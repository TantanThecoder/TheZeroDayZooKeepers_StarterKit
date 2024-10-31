import paramiko
import paramiko.ssh_exception
import logging
from Validator.validator import Validator
import sys

logging.basicConfig(level=logging.INFO)
class Ssh:

    def __init__(self, ssh=None):
        self.ssh = ssh if ssh else paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    def ssh_validate_ip(self, ip):
        """
        Uses validator class to check that ip adress is valid. If not, lets user input ip adress again,
        or terminate the program!
        
         Args:
            - Ip: The ip adress to be checked.

         Returns:
            - Ip: The new validated ip is returned. 
        """
        while True:
            if not Validator.validate_ip(ip):
                logging.error(f"Invalid ip adress, double check and try again: {ip}")
                ip = input("Enter the ip adress again:")
            else:
                break
        return ip

    def ssh_validate_path(self, local_path, remote_path):
        """
        Quick check that both local_path and remote_path is valid paths!
        Terminates program if either is invalid.

         Args:
            - local_path: The path on the local computer where the downloaded file is saved.
            - remote_path: The path on the ssh server where the file to be downloaded is stored.

        Returns:
            - None: Simply returns back to continue the next code line if no errors occured.
        """
        if not Validator.validate_path(local_path):
            logging.error(f"The local path: {local_path} was invalid, please double check the path!")
            sys.exit("Teminating program due to invalid path!")
        if not Validator.validate_path(remote_path):
            logging.error(f"The remote path: {remote_path} was invalid, please double check the path!")
            sys.exit("Teminating program due to invalid path!")
        return

    def ssh_connect(self, ip, user, password):
        """
        Establishes a connection to the ssh based on inputs.

         Args:
            - ip (str): The IP address of the SSH server.
            - user (str): The username to log in to the SSH server.
            - password (str): The password for the chosen username.
        """
        print("stop4")
        try:
            self.ssh.connect(ip, username=user, password=password)
            logging.info(f"We have a connection to {user}@{ip}")
            print(f"We have a connection to {user}@{ip}")
        except paramiko.AuthenticationException:
            logging.error("Failed to authenticate!")

    def ssh_sftp(self, local_path, remote_path, action):
        """
        Takes the established ssh connection and opens a new sftp connection to manage upload or download.

         Args:
            - local_path (str): The local file path for upload or download.
            - remote_path (str): The remote file path for upload or download.
            - action (str): The action to perform ('upload' or 'download').
        """
        try:
            sftp = self.ssh.open_sftp()
            logging.info("We have a sftp connection.")

            if action == "upload":
                sftp.put(local_path, remote_path)
                logging.info(f"The file: {local_path} have been uploaded to the remote path: {remote_path}")
            elif action == "download":
                sftp.get(remote_path, local_path)
                logging.info(f"The file: {remote_path} have been downloaded to the local path: {local_path}")
        except TypeError as e:
            logging.error(f"Missing a path: {e}")
        except PermissionError:
            logging.error(f"Missing permission to make this action!")
        except FileNotFoundError:
            logging.error(f"No file with that path/name! : {local_path}, or the target path is invalid : {remote_path}. Please check the paths again!")
        finally:
            sftp.close()


    def ssh_script_file_unpack(self, script_file):
        """
        Take the file for the given script and unpacks it to a list.
         
         Args:
            - script: Name of the file the script is contained in.

         Returns:
            - list: A list of strings, each representing a line in the script file.
        """
        try:
            with open(script_file, 'r') as file:
                script = [line.strip() for line in file]
        except FileNotFoundError:
            logging.error(f"Could not find the specified file: {script_file}. Please check the path and try again.")
        except Exception as e:
            logging.error(f"Unexcpected error: {e}")
        return script


    def ssh_script(self, ip, user, password, script):
        """
        Sends a connection request to ssh_connect followed by an Execute of the sent in script.
         
         Args
            - ip: The ip adress of the ssh server.
            - user: The username to login to the ssh server with.
            - password: The password for the choosen username.
            - script: The path or name of the file containing the script.
        """
        print("stop3")
        try:
            self.ssh_connect(ip, user, password)
            formated_script = self.ssh_script_file_unpack(script)
            print(formated_script)
            logging.info("Executing script")

            for command in formated_script:
                if command.startswith("#") or not command:
                    continue
            
                stdin, stdout, stderr = self.ssh.exec_command(formated_script)

                output = stdout.read().decode()
                error = stderr.read().decode()

                if output:
                    logging.info(output)
                elif error:
                    logging.error(f"Error: {error}")
        except TypeError:
            logging.error("Failed to execute script/command since it might be None!")
        except Exception as e:
            logging.error(f"Unexpected error occured: {e}")
        finally:
            self.ssh.close()

    
    def ssh_upload(self, ip, user, password, local_path, remote_path):
        """
        Execute upload request to the ssh server based on given paths

         Args:
            - ip: The ip adress of the ssh server.
            - user: The username to login to the ssh server with.
            - password: The password for the choosen username.
            - local_path: Name or path on the local computer where the file to be uploaded is stored.
            - remote_path: The path on the ssh server where the file will be uploaded to.
        """
        self.ssh_validate_path(local_path, remote_path)

        try:

            self.ssh_connect(ip, user, password)
            self.ssh_sftp(local_path, remote_path, "upload")

        except Exception as e:
            logging.error(f"Unexcpected error occured: {e}")
        finally:
            self.ssh.close()


    def ssh_download(self, ip, user, password, local_path, remote_path):
        """
        Execute download request from ssh server based on given paths

         Args:
            - ip: The ip adress of the ssh server.
            - user: The username to login to the ssh server with.
            - password: The password for the choosen username.
            - local_path: The path on the local computer where the downloaded file is saved.
            - remote_path: The path on the ssh server where the file to be downloaded is stored.

        """
        self.ssh_validate_path(local_path, remote_path)

        try:
            self.ssh_connect(ip, user, password)
            self.ssh_sftp(local_path, remote_path, "download")

        except Exception as e:
            logging.error(f"Unexcpected error occured: {e}")
        finally:
            self.ssh.close()


    def Main(self, action, ip, username, password, script, local_path, remote_path):

        valid_ip = self.ssh_validate_ip(ip)

        if action == "script":
            print("stop2")
            self.ssh_script(valid_ip, username, password, script)
        elif action == "upload":
            if not Validator.validate_non_empty(local_path) or not Validator.validate_non_empty(remote_path):
                logging.warning("Invalid Path, exiting program!")
                sys.exit(0)
            self.ssh_upload(valid_ip, username, password, local_path, remote_path)
        elif action == "download":
            if not Validator.validate_non_empty(local_path) or not Validator.validate_non_empty(remote_path):
                logging.warning("Invalid Path, exiting program!")
                sys.exit(0)
            self.ssh_download(valid_ip, username, password, local_path, remote_path)






try:
    import nmap
except ImportError:
    logging.error("Nmap library is not installed! Please run 'pip install python-nmap'.")
import json
import logging
from pathlib import Path
from Validator.validator import Validator
from Json_config.json_config import Json_config
import sys

json_config = Json_config()
json_get = json_config.load_config()



class Scanner:
    def __init__(self, port_scanner=None):
        self.scanner = port_scanner if port_scanner else nmap.PortScanner()
        self.path = Path.cwd() / "Scanner" / "Scanner_files"


    def write_file(self, formated_result, output_file):
        """
        Used to write output from scans into .txt files.

         Args:
            - formated_result: The returned value from fuction format_scan(), formated for better readability
            - output_file: Name of the file the function write formated_result to.
        """
        if json_get.get("scanner_path_default"):
            try:
                with open(self.path / output_file, 'a') as file:
                    file.write(formated_result)
            except FileNotFoundError:
                logging.error(f" Could not find the specified file: {output_file}. Please check the path and try again.\n")
            except PermissionError as e:
                logging.error(f" Permission denied: {e}\n")
            except Exception as e:
                logging.error(f" An error occured, {e}\n")
        else: 
            try:
                with open(output_file, 'a') as file:
                    file.write(formated_result)
            except FileNotFoundError:
                logging.error(f" Could not find the specified file: {output_file}. Please check the path and try again.\n")
            except PermissionError as e:
                logging.error(f" Permission denied: {e}\n")
            except Exception as e:
                logging.error(f" An error occured, {e}\n")

    def format_scan(self, output):
        """
        Formats the result from scan to make it more readable.
         
         Args:
            - ouput: The result given from the scan.

         Returns:
            - String: A string of the output in a formated form
        """
        formated_result = json.dumps(output, indent=4)
        return formated_result

    def read_file(self, file_name):
        """
        Reads a given file meant to contain ip adresses and returns a list of said ip adresses

         Args:
            - file_name: Name of the file containing the desired ip adresses
        """
        if json_get.get("scanner_path_default"):
            try:
                logging.info(f" Reading file: {file_name}\n")
                with open(self.path / file_name, 'r') as file:
                    hosts = [line.strip() for line in file.readlines()]
                    return hosts
            except FileNotFoundError:
                logging.error(f" Could not find the specified file: {file_name}. Please check the path and try again.\n")
                sys.exit("Terminating program as it cant proceed!")
            except PermissionError as e:
                logging.error(f" Permission denied: {e}\n")
                sys.exit("Terminating program as it cant proceed!")
            except Exception as e:
                logging.error(f" Unexpected error: {e}\n")
                sys.exit("Terminating program as it cant proceed!")
        else: 
            try:
                logging.info(f" Reading file: {file_name}\n")
                with open(file_name, 'r') as file:
                    hosts = [line.strip() for line in file.readlines()]
                    return hosts
            except FileNotFoundError:
                logging.error(f" Could not find the specified file: {file_name}. Please check the path and try again.\n")
                sys.exit("Terminating program as it cant proceed!")
            except PermissionError as e:
                logging.error(f" Permission denied: {e}\n")
                sys.exit("Terminating program as it cant proceed!")
            except Exception as e:
                logging.error(f" Unexpected error: {e}\n")
                sys.exit("Terminating program as it cant proceed!")

    def Scan_file(self, file_name, output_file, flags=None):
        """
        Scans hosts from the input file using Nmap and writes results to an output file.

         Args:
            - file_name: File containing host addresses to scan.
            - output_file: File to store scan results.
            - flags: Optional Nmap flags for advanced scanning options.
        """
        hosts = self.read_file(file_name)
        for host in hosts:
            if not Validator.validate_ip(host):
                logging.warning(f" Skipping scan for {host} and continuing to next host!\n")
                continue
            try:
                if flags == None:
                    logging.info(f" Started scan for host: {host}\n")
                    self.scanner.scan(host) 
                else:
                    logging.info(f"Starting scan for host: {host}, with flags: {flags}\n")
                    self.scanner.scan(host, arguments=flags)
            except nmap.PortScannerError as e:
                logging.error(f" An Nmap error occured: {e}\n")
            except Exception as e:
                logging.error(f" An error occurred! {e}\n")
            else:
                if host in self.scanner.all_hosts():
                    output = self.scanner[host]
                # Check if the host is up before formatting and writing
                    if self.scanner[host].state() == "up":
                        logging.info(f"Scan for host: {host}, successful!\n")
                        formatted_result = self.format_scan(output)
                        self.write_file(formatted_result, output_file)
                    else:
                        logging.info(f"Host {host} is down, skipping writing results.\n")
                else:
                    logging.info(f"Host {host} was not found in scan results, skipping.\n")


        logging.info(f" A file has been created with the given name: {output_file}")

    def Scan_terminal(self, host, output_file, flags):
        """
        Scans a host or range of hosts entered via terminal input using Nmap and stores results.

         Args:
            - input: Host or IP range to scan.
            - output_file: File to store scan results.
            - flags: Optional Nmap flags for advanced scanning options.
        """
        
        while True:
            if not Validator.validate_ip(host):
                host = input(f"Invalid ip adress: {host}, please enter a new ip adress or type exit to terminate program:")
            else:
                break
            if host.lower() == "exit":
                    sys.exit("Terminating program as per request.")
        try:
            if flags == None:
                logging.info(f" Starting scan for host: {host}\n")
                self.scanner.scan(host)
            else:
                logging.info(f" Starting scan for host: {host}, with flags: {flags}\n")
                self.scanner.scan(host, arguments=flags)
        except Exception as e:
            logging.error(f" An error occurred! {e}\n")

        output = self.scanner[host]
        formated_result = self.format_scan(output)
        self.write_file(formated_result, output_file)
        
        logging.info(f" A file has been created with the given name: {output_file}")    

    def Main(self, action, input, output_file, flags=None):
        if action == "file":
            self.Scan_file(input, output_file, flags)
        elif action =="terminal_input":
            self.Scan_terminal(input, output_file, flags)


    

"""
TODO:
Add ip-validation
"""
try:
    import nmap
except ImportError:
    logging.error("Nmap library is not installed! Please run 'pip install python-nmap'.")

import json
import logging

class Scanner:
    def __init__(self, port_scanner=None):
        self.scanner = port_scanner if port_scanner else nmap.PortScanner()


    def write_file(self, formated_result, output_file):
        """
        Used to write output from scans into .txt files
        -formated_result: The returned value from fuction format_scan(), formated for better readability
        -output_file: Name of the file the function write formated_result to.
        """
        try:
            with open(output_file, 'a') as file:
                file.write(formated_result)
        except FileNotFoundError:
            logging.error(f"Error opening file: {output_file}")
        except PermissionError as e:
            logging.error(f"Permission denied: {e}")
        except Exception as e:
            logging.error(f"An error occured, {e}")

    def format_scan(self, output):
        """
        Formats the result from scan to make it more readable.
        -ouput: The result given from the scan.
        """
        formated_result = json.dumps(output, indent=4)
        return formated_result

    def read_file(self, file_name):
        """
        Reads a given file meant to contain ip adresses and returns a list of said ip adresses
        -file_name: Name of the file containing the desired ip adresses
        """
        logging.info(f"\n Reading file: {file_name}\n")
        try:
            with open(file_name, 'r') as file:
                hosts = [line.strip() for line in file.readlines()]
                return hosts
        except FileNotFoundError:
            logging.error(f"No file found with the inputed name: {file_name}")
        except PermissionError as e:
            logging.error(f"Permission denied: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")


    def Scan_file(self, file_name, output_file, flags=None):
        """
        Scans hosts from the input file using Nmap and writes results to an output file.
        Parameters:
        - file_name: File containing host addresses to scan.
        - output_file: File to store scan results.
        - flags: Optional Nmap flags for advanced scanning options.
        """
        logging.info("Scanning...")
        hosts = self.read_file(file_name)
        for host in hosts:
            try:
                if flags == None:
                    self.scanner.scan(host)
                else:
                    self.scanner.scan(host, flags)
            except nmap.PortScannerError as e:
                logging.error(f"An Nmap error occured: {e}")
            except Exception as e:
                logging.error(f"An error occurred! {e}")

            output = self.scanner[host]
            formated_result = self.format_scan(output)
            self.write_file(formated_result, output_file)

        logging.info(f"A file has been created with the given name: {output_file}")

    def Scan_terminal(self, input, output_file, flags):
        """
        Scans a host or range of hosts entered via terminal input using Nmap and stores results.
        Parameters:
        - input: Host or IP range to scan.
        - output_file: File to store scan results.
        - flags: Optional Nmap flags for advanced scanning options.
        """
        logging.info("Scanning...")
        try:
            if flags == None:
                self.scanner.scan(input)
            else:
                self.scanner.scan(input, flags)
        except Exception as e:
            logging.error(f"An error occurred! {e}")

        output = self.scanner[input]
        formated_result = self.format_scan(output)
        self.write_file(formated_result, output_file)
        
        logging.info(f"A file has been created with the given name: {output_file}")    

    def Main(self, action, input, output_file, flags=None):
        if action == "File":
            self.Scan_file(input, output_file, flags)
        elif action =="Terminal_input":
            self.Scan_terminal(input, output_file, flags)


    

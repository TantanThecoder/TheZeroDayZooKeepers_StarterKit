import argparse
import nmap
import json

#parser = argparse.ArgumentParser(description="Script for executing a Nmap Scan and generating a file with the result")

#subparser = parser.add_subparsers(title="Options", dest="command", help="Decide how to input the host adresses!")

#parser_multiple = subparser.add_parser("File", help="Take a file of hosts as input to scan!")
#parser_multiple.add_argument("File_name", help="Enter the name of the file containing the host adresses to be scanned!")
#parser_multiple.add_argument("Output_file", help="Name of the file to store the output in")
#parser_multiple.add_argument("-f", "--flags", help="Add desired flags for the scan, optinal!")


#parser_singular = subparser.add_parser("Teminal", help="Enter a range of hosts to scan or a single host directly into the terminal as an argument")
#parser_singular.add_argument("host", help="Enter the host ip!")
#parser_singular.add_argument("Output_file", help="Name of the file to store the output in")
#parser_singular.add_argument("-f", "--flags", help="Add desired flags for the scan, optional!")



#args= parser.parse_args()
class Scanner:
    def __init__(self) -> None:
        self.scanner = nmap.PortScanner()


    def write_file(formated_result, output_file):
        try:
            with open(output_file, 'a') as file:
                file.write(formated_result)
        except Exception as e:
            print(f"Unexpected error: {e}")

    def format_scan(output):
            formated_result = json.dumps(output, indent=4)
            return formated_result

    def read_file(self, file_name):
        print(f"\n Läser fil: {file_name}\n")
        try:
            with open(file_name, 'r') as file:
                hosts = [line.strip() for line in file.readlines()]
                return hosts
        except FileNotFoundError:
            print(f"No file found with the inputed name: {file_name}")
        except Exception as e:
            print(f"Unexpected error: {e}")


    def Scan_file(self, file_name, output_file, flags):
        print("Scanning...")
        hosts = self.read_file(file_name)
        for host in hosts:
            try:
                if flags == None:
                    self.scanner.scan(host)
                else:
                    self.scanner.scan(host, flags)
            except Exception as e:
                print(f"An error occurred! {e}")
            output = self.scanner[host]
            formated_result = self.format_scan(output)
            self.write_file(formated_result, output_file)
        print(f"A file has been created with the given name: {output_file}")

    def Scan_terminal():
        print("Scanning...")    

    def Main(self, action, input, output_file, flags):
        if action == "File":
            self.Scan_file(input, output_file, flags)
        elif action =="Terminal":
            self.Scan_terminal()


    

import argparse
import nmap
import json

parser = argparse.ArgumentParser(description="Script for executing a Nmap Scan and generating a file with the result")

subparser = parser.add_subparsers(title="Options", dest="command", help="Decide how to input the host adresses!")

parser_multiple = subparser.add_parser("File", help="Take a file of hosts as input to scan!")
parser_multiple.add_argument("File_name", help="Enter the name of the file containing the host adresses to be scanned!")
parser_multiple.add_argument("Output_file", help="Name of the file to store the output in")
parser_multiple.add_argument("-f", "--flags", help="Add desired flags for the scan, optinal!")


parser_singular = subparser.add_parser("Teminal", help="Enter a range of hosts to scan or a single host directly into the terminal as an argument")
parser_singular.add_argument("host", help="Enter the host ip!")
parser_singular.add_argument("Output_file", help="Name of the file to store the output in")
parser_singular.add_argument("-f", "--flags", help="Add desired flags for the scan, optional!")



args= parser.parse_args()

scanner = nmap.PortScanner()

def write_file(input):
    try:
        with open(args.Output_file, 'a') as file:
            file.write(input)
    except Exception as e:
        print(f"Unexpected error: {e}")

def format_scan(output):
        formated_result = json.dumps(output, indent=4)
        return formated_result

def read_file():
    print(f"\n Läser fil: {args.File_name}\n")
    try:
        with open(args.File_name, 'r') as file:
            hosts = [line.strip() for line in file.readlines()]
            return hosts
    except FileNotFoundError:
        print(f"No file found with the inputed name: {args.File_name}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def format_options():
    options = args.flags
    options_formated = options.replace("_", " ")
    return options_formated

def Scan_file():
    print("Scanning...")
    hosts = read_file()
    for host in hosts:
        try:
            if args.flags == None:
                scanner.scan(host)
            else:
                scanner.scan(host, args.flags)
        except Exception as e:
            print(f"An error occurred! {e}")
        output = scanner[host]
        formated_result = format_scan(output)
        write_file(formated_result)
    print(f"A file has been created with the given name: {args.Output_file}")

def Scan_terminal():
    print("Scanning...")    

def Main():
    if args.command == "File":
        Scan_file()
    elif args.command =="Terminal":
        Scan_terminal()

if __name__ == "__main__":
    Main()
    

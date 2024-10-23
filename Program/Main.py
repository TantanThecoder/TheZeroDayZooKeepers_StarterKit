import argparse
from Cipher import Cipher
from Keygen import Keygen
from Scanner import Scanner

parser = argparse.ArgumentParser(description="A hackers tool with multiple choices of Scripts!")

subparser = parser.add_subparsers(title="Options", dest="command", help="Choose what script to run!")

parser_scanner = subparser.add_parser("Scanner", help="Take a file of hosts as input to scan!")
parser_scanner.add_argument("Action", choices=["File", "Terminal_input"], help="Choose wether to scan host take from a file or input the host in the terminal!")
parser_scanner.add_argument("Input", help="Enter the name of the file containing the host adresses to be scanned!")
parser_scanner.add_argument("Output_file", help="Name of the file to store the output in")
parser_scanner.add_argument("-f", "--flags", help="Add desired flags for the scan, optinal!")

parser_key = subparser.add_parser("Keygen", help="Generate a Cipher key to encrypt or decrypt data")
parser_key.add_argument("-f", "--file_name", help="Enter the name of the file to store the key in! If not entered a defult name will be given!", default="generated.key")

parser_cipher = subparser.add_parser("Cipher", help="Encrypt or Decrypt a file or input text")
parser_cipher.add_argument("Action", choices=["Decrypt", "Encrypt"], help="Choose wether to use encrypt or decrypt")
parser_cipher.add_argument("Data_type", choices=["File", "Terminal_input"], help="Choose wether to encrypt text from a file or direct input to terminal!")
parser_cipher.add_argument("Input", help="Takes the name of the file or terminal input to be encrypted!")
parser_cipher.add_argument("File_name", help="Name of the file the output is stored in")
parser_cipher.add_argument("-k", "--key", help="Enter the name of the file containing the cryptography key, if default key name is in use, this option becomes optional", default="generated.key")

args = parser.parse_args()

def Main():
    if args.command == "Scanner":
        scanner = Scanner()
        scanner.Main(args.Input, args.Output_file, args.flags)
        print("Scanner")
    elif args.command == "Keygen":
        keygen = Keygen()
        keygen.Main(args.file_name)
        print("Key")
    elif args.command == "Cipher":
        cipher = Cipher()
        cipher.Main(args.Action, args.Data_type, args.Input, args.File_name, args.key)
        print("Cipher")

if __name__ == "__main__":
    Main()
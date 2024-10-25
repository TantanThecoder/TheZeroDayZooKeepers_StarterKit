import argparse
from Cipher.cipher import Cipher
from Cipher.keygen import Keygen
from Scanner.scanner import Scanner
from Enumeration.enumeration import Enumeration
import json

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

config = load_config()


parser = argparse.ArgumentParser(description="A hacker's tool with multiple scripts for various tasks.")

subparser = parser.add_subparsers(title="Options", dest="command", help="Select what script to run!")

parser_scanner = subparser.add_parser("Scanner", help="Scan hosts for open ports and services.")
parser_scanner.add_argument("Action", choices=["File", "Terminal_input"], help="Specify the source of hosts to scan: 'File' for a file containing host addresses or 'Terminal_input' for manual entry.")
parser_scanner.add_argument("Input", help="The file name containing host addresses (if Action is 'File') or the host IP address (if Action is 'Terminal_input').")
parser_scanner.add_argument("-o","--output_file", help="The name of the file where the scan results will be saved. A default name will be given if this flag is not in use!", default=config.get("default_output_file"))
parser_scanner.add_argument("-f", "--flags", help="Optional: Add desired flags for the Nmap scan (e.g., '-sS' for SYN scan).", default=config.get("default_nmap_flags"))

parser_key = subparser.add_parser("Keygen", help="Generate a Cipher key to use for encrypting or decrypting data")
parser_key.add_argument("-k", "--key_file", help="Enter the name of the file to store the key in! If not entered a defult name will be given!", default=config.get("default_cipher_key_file"))

parser_cipher = subparser.add_parser("Cipher", help="Encrypt or Decrypt a file or input text")
parser_cipher.add_argument("Action", choices=["Decrypt", "Encrypt"], help="Choose wether to use encrypt or decrypt")
parser_cipher.add_argument("Data_type", choices=["File", "Terminal_input"], help="Choose wether to encrypt text from a file or direct input to terminal!")
parser_cipher.add_argument("Input", help="The file name containing message to be ciphered (if Action is 'File') or direct input (if Action is 'Terminal_input').")
parser_cipher.add_argument("-o","--output_file", help="The name of the file where the ciphered message is stored.", default=config.get("default_output_file"))
parser_cipher.add_argument("-k", "--key", help="Enter the name of the file containing the cryptography key, if default key name is in use, this option becomes optional.", default=config.get("default_cipher_key_file"))

parser_enumeration = subparser.add_parser("Enumerate", help="Run subdomain enumeration on a website")
parser_enumeration.add_argument("Domain", help="Enter the webiste to run subdomain enumeration on!")
parser_enumeration.add_argument("-o", "--output_file", help="Enter the desired name for the output file! A default name will be given if this flag is not in use!", default=config.get("default_output_file"))
parser_enumeration.add_argument("-t", "--thread", help="Enter desired thread, default thread is set at 20!", default=config.get("enumeration_thread_option"))

args = parser.parse_args()

def Main():
    if args.command == "Scanner":
        scanner = Scanner()
        scanner.Main(args.Action, args.Input, args.output_file, args.flags)
    elif args.command == "Keygen":
        keygen = Keygen()
        keygen.Main(args.key_file)
    elif args.command == "Cipher":
        cipher = Cipher()
        cipher.Main(args.Action, args.Data_type, args.Input, args.output_file, args.key)
    elif args.command == "Enumerate":
        enumeration = Enumeration()
        enumeration.Main(args.Domain, args.thread, args.output_file)

if __name__ == "__main__":
    Main()
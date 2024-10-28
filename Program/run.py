import argparse
from Cipher.cipher import Cipher
from Cipher.keygen import Keygen
from Scanner.scanner import Scanner
from Enumeration.enumeration import Enumeration
from SSH.ssh import Ssh
from Json_config.json_config import Json_config
import logging
import sys

VERSION = "Alpha 0.9.5"

json_config = Json_config()
json_get = json_config.load_config()

if not json_get:
    logging.error("Configuration file 'config.json' is missing or invalid. Please create it with default settings or check github for correct file!")
    sys.exit("Exiting due to configuration error.")


parser = argparse.ArgumentParser(description="A hacker's tool with multiple scripts for various tasks.")
parser.add_argument('-v','--version', action='version', version=f'ZeroDayZooKeepers {VERSION}')

subparser = parser.add_subparsers(title="Options", dest="script", help="Select what script to run!")

parser_scanner = subparser.add_parser("scanner", help="Scan hosts for open ports and services.")
parser_scanner.add_argument("action", choices=["file", "terminal_input"], help="Specify the source of hosts to scan: 'File' for a file containing host addresses or 'Terminal_input' for manual entry.")
parser_scanner.add_argument("input", help="The file name containing host addresses (if Action is 'File') or the host IP address (if Action is 'Terminal_input').")
parser_scanner.add_argument("-o","--output_file", help="The name of the file where the scan results will be saved. A default name will be given if this flag is not in use!", default=json_get.get("default_output_file"))
parser_scanner.add_argument("-f", "--flags", help="Optional: Add desired flags for the Nmap scan (e.g., '-sS' for SYN scan).", default=json_get.get("default_nmap_flags"))

parser_key = subparser.add_parser("keygen", help="Generate a Cipher key to use for encrypting or decrypting data")
parser_key.add_argument("-k", "--key_file", help="Enter the name of the file to store the key in! If not entered a defult name will be given!", default=json_get.get("default_cipher_key_file"))

parser_cipher = subparser.add_parser("cipher", help="Encrypt or Decrypt a file or input text")
parser_cipher.add_argument("action", choices=["decrypt", "encrypt"], help="Choose wether to use encrypt or decrypt")
parser_cipher.add_argument("data_type", choices=["file", "terminal_input"], help="Choose wether to encrypt text from a file or direct input to terminal!")
parser_cipher.add_argument("input", help="The file name containing message to be ciphered (if Action is 'File') or direct input (if Action is 'Terminal_input').")
parser_cipher.add_argument("-o","--output_file", help="The name of the file where the ciphered message is stored.", default=json_get.get("default_output_file"))
parser_cipher.add_argument("-k", "--key", help="Enter the name of the file containing the cryptography key, if default key name is in use, this option becomes optional.", default=json_get.get("default_cipher_key_file"))

parser_enumeration = subparser.add_parser("enumerate", help="Run subdomain enumeration on a website")
parser_enumeration.add_argument("domain", help="Enter the webiste to run subdomain enumeration on!")
parser_enumeration.add_argument("-o", "--output_file", help="Enter the desired name for the output file! A default name will be given if this flag is not in use!", default=json_get.get("default_output_file"))
parser_enumeration.add_argument("-t", "--thread", help="Enter desired thread count, the default thread can be changed in config.json!", default=json_get.get("enumeration_thread_option"))

parser_ssh = subparser.add_parser("ssh", help="Connect and make automated actions on ssh servers.")
parser_ssh.add_argument("action", choices=["script", "upload", "download"], help="Specify the action to perform: 'script' to execute a script, 'upload' to upload a file to the ssh server, or 'download' to download a file from the ssh server.")
parser_ssh.add_argument("ip", help="The ip adress for the ssh server.")
parser_ssh.add_argument("username", help="The login username for the requested ssh server")
parser_ssh.add_argument("password", help="The login password for the requested ssh server")
parser_ssh.add_argument("-s", "--script", help="The path or name of the file containing the script to be executed (required if action is 'script', default script can be set in config.json).", default=json_config.raw_to_universal_path(json_get.get("ssh_default_script")))
parser_ssh.add_argument("-l", "--local_path", help= "The path on the local machine where the file will be saved or retrieved from.(Requierd if action is 'upload' or 'download', a default local_path can be set in config.json)", default=json_config.raw_to_universal_path(json_get.get("ssh_default_local_path")))
parser_ssh.add_argument("-r", "--remote_path", help= "The path on the SSH server where the file will be uploaded or downloaded from.(Requierd if action is 'upload' or 'download', a default remote_path can be set in config.json)", default=json_config.raw_to_universal_path(json_get.get("ssh_default_remote_path")))

args = parser.parse_args()

def Main():
    if args.script == "scanner":
        scanner = Scanner()
        scanner.Main(args.action, args.input, args.output_file, args.flags)
    elif args.script == "keygen":
        keygen = Keygen()
        keygen.Main(args.key_file)
    elif args.script == "cipher":
        cipher = Cipher()
        cipher.Main(args.action, args.data_type, args.input, args.output_file, args.key)
    elif args.script == "enumerate":
        enumeration = Enumeration()
        enumeration.Main(args.domain, args.thread, args.output_file)
    elif args.script == 'ssh':
        ssh = Ssh()
        ssh.Main(args.action, args.ip, args.username, args.password, args.script, args.local_path, args.remote_path)


if __name__ == "__main__":
    Main()
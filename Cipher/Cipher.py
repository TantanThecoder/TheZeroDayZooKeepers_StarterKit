from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser(description="Decrypt or encrypt a file!")

subparser = parser.add_subparsers(title="Subcommands", dest="command", help="Choose whether you wanna encrypt or decrypt")

parser_encrypt = subparser.add_parser("Encrypt", help="Encrypt a file or input text")
parser_encrypt.add_argument("Data_type", choices=["File", "Terminal_input"], help="Choose wether to encrypt text from a file or direct input to terminal!")
parser_encrypt.add_argument("Input", help="Takes the name of the file or terminal input to be encrypted!")
parser_encrypt.add_argument("File_name", help="Name of the file the output is stored in")
parser_encrypt.add_argument("-k", "--key", help="Enter the name of the file containing the cryptography key, if default key name is in use, this option becomes optional", default="generated.key")

parser_decrypt = subparser.add_parser("Decrypt", help="Decrypt a file")
parser_decrypt.add_argument("Data_type", choices=["File", "Terminal_input"], help="Choose wether to decrypt text from a file or direct input to terminal!")
parser_decrypt.add_argument("Input", help="Takes the name of the file or terminal input to be decrypted!")
parser_decrypt.add_argument("File_name", help="Name of the file the output is stored in")
parser_decrypt.add_argument("-k", "--key", help="Enter the name of the file containing the cryptography key, if default key name is in use, this option becomes optional", default="generated.key")

args = parser.parse_args()

def Encrypt(cipher_suite):
    if args.Data_type == "File":
        try:
            with open(args.Input, "rb") as text_file:
                message = text_file.read()
                cipher_text = cipher_suite.encrypt(message)
        except FileNotFoundError:
            print("Invalid file name!")
        else:
            print("File has been read!")
    else:
        message = args.Input.encode()
        cipher_text = cipher_suite.encrypt(message)

    if ".enc" in args.File_name:
        with open(args.File_name, "wb") as encrypt_file:
            encrypt_file.write(cipher_text)
    else:
        edited_file_name = args.File_name + ".enc"
        with open(edited_file_name, "wb") as encrypt_file:
            encrypt_file.write(cipher_text)

def Decrypt(cipher_suite):
    try:
        with open(args.Input, "rb") as encrypted_file:
            encrypterd_text = encrypted_file.read()
    except FileNotFoundError:
        print(f"The file: {args.Input} was not found!")
    else:
        decrypted_text = cipher_suite.decrypt(encrypterd_text)

        with open(args.File_name, "wb") as decrypted_file:
            decrypted_file.write(decrypted_text)


def Main():
    try:
        with open(args.key, "rb") as key_file:
            cipher_key = key_file.read()
    except FileNotFoundError:
        print(f"The file: {args.key} was not found!")
    else:
        cipher_suite = Fernet(cipher_key)

    if args.command == "Decrypt":
        Decrypt(cipher_suite)

    elif args.command == "Encrypt":
        Encrypt(cipher_suite)

if __name__ == "__main__":
    Main()


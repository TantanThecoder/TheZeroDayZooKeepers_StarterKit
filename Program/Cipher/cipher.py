try:
    from cryptography.fernet import Fernet
except ImportError:
    logging.error("Cryptography library missing! Please run 'pip install cryptography'")
import logging

"""
TODO
Load config file containing preset file names
"""

class Cipher:
    def __init__(self) -> None:
        pass

    def Encrypt(self, cipher_suite, input, file_name, data_type):
        """
        Encrypts the given input using the provided cipher_suite.
        Parameters:
        - cipher_suite: Fernet encryption suite.
        - input: Input text or file to be encrypted.
        - file_name: Output file to save the encrypted content.
        - data_type: Specifies whether input is from a file or terminal input.
        """
        if data_type == "File":
            try:
                with open(input, "rb") as text_file:
                    message = text_file.read()
                    cipher_text = cipher_suite.encrypt(message)
            except FileNotFoundError:
                logging.error("Invalid file name!")
            else:
                logging.info("File has been read!")
        else:
            message = input.encode()
            cipher_text = cipher_suite.encrypt(message)

        if ".enc" in file_name:
            with open(file_name, "wb") as encrypt_file:
                encrypt_file.write(cipher_text)
        else:
            edited_file_name = file_name + ".enc"
            with open(edited_file_name, "wb") as encrypt_file:
                encrypt_file.write(cipher_text)

    def Decrypt(self, cipher_suite, input, file_name, data_type):
        """
        Decrypts the given input using the provided cipher_suite.
        Parameters:
        - cipher_suite: Fernet encryption suite.
        - input: Input text or file name to be decrypted.
        - file_name: Output file to save the decrypted content.
        - data_type: Specifies whether input is from a file or terminal input.
        """
        if data_type == "File":
            try:
                with open(input, "rb") as encrypted_file:
                    encrypterd_text = encrypted_file.read()
            except FileNotFoundError:
                logging.error(f"The file: {input} was not found!")
            else:
                decrypted_text = cipher_suite.decrypt(encrypterd_text)
            
        else:
            message = input.encode()
            decrypted_text = cipher_suite.decrypt(message)
        
        with open(file_name, "wb") as decrypted_file:
                    decrypted_file.write(decrypted_text)


    def Main(self, action, data_type, input, file_name, key):
        """
        Main method for handling encryption and decryption.
        Parameters:
        - action: Specifies whether to Encrypt or Decrypt.
        - data_type: Source of data (File or Terminal Input).
        - input: The input data or file to be encrypted/decrypted.
        - file_name: Name of the file to store output in.
        - key: The cryptographic key used for encryption/decryption.
        """
        try:
            with open(key, "rb") as key_file:
                cipher_key = key_file.read()
        except FileNotFoundError:
            logging.error(f"The file: {key} was not found!")
        else:
            cipher_suite = Fernet(cipher_key)

        if action == "Decrypt":
            self.Decrypt(cipher_suite, input, file_name, data_type)

        elif action == "Encrypt":
            self.Encrypt(cipher_suite, input, file_name, data_type)


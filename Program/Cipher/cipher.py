try:
    from cryptography.fernet import Fernet
except ImportError:
    logging.error("Cryptography library missing! Please run 'pip install cryptography'")
import logging

class Cipher:
    def __init__(self) -> None:
        pass

    def Encrypt(self, cipher_suite, input, file_name, data_type):
        """
        Encrypts the given input using the provided cipher_suite.

         Args:
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
                    #validate message or cipher text == none
            except FileNotFoundError:
                logging.error(f"Could not find the specified file: {input}. Please check the path and try again.")
            else:
                logging.info("File has been read!")
        else:
            message = input.encode()
            cipher_text = cipher_suite.encrypt(message)
            #validate message or cipher text == none

        if ".enc" in file_name:
            with open(file_name, "wb") as encrypt_file:
                encrypt_file.write(cipher_text)
        else:
            edited_file_name = file_name + ".enc"
            with open(edited_file_name, "wb") as encrypt_file:
                encrypt_file.write(cipher_text)
            #More comprehensive test for certain file types. Does it matter what type of file it is?

    def Decrypt(self, cipher_suite, input, file_name, data_type):
        """
        Decrypts the given input using the provided cipher_suite.

         Args:
            - cipher_suite: Fernet encryption suite.
            - input: Input text or file name to be decrypted.
            - file_name: Output file to save the decrypted content.
            - data_type: Specifies whether input is from a file or terminal input.
        """
        decrypted_text = None

        if data_type == "File":
            try:
                with open(input, "rb") as encrypted_file:
                    encrypted_text = encrypted_file.read()
                    if not encrypted_text:  # Check if the file is empty
                        logging.error(f"The file {input} is empty.")
                        return
                    #validate not none?
            except FileNotFoundError:
                logging.error(f"Could not find the specified file: {input}. Please check the path and try again.")
                return
            else:
                decrypted_text = cipher_suite.decrypt(encrypted_text)
            
        else:
            message = input.encode()
            decrypted_text = cipher_suite.decrypt(message)
            #validate input not none?
        
        #validate filename?
        if decrypted_text is not None:
            with open(file_name, "wb") as decrypted_file:
                decrypted_file.write(decrypted_text)


    def Main(self, action, data_type, input, file_name, key):
        """
        Main method for handling encryption and decryption.

         Args:
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
            logging.error(f"Could not find the specified file: {key}. Please check the path and try again.")
        else:
            cipher_suite = Fernet(cipher_key)

        if action == "Decrypt":
            self.Decrypt(cipher_suite, input, file_name, data_type)

        elif action == "Encrypt":
            self.Encrypt(cipher_suite, input, file_name, data_type)


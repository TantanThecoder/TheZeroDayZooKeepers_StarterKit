from Cipher.cipher import Cipher
from Cipher.keygen import Keygen
from cryptography.fernet import Fernet
import unittest
import os

class TestCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = Cipher()
        self.keygen = Keygen()
        self.keygen.Main("test_key.key")
        self.key = "test_key.key"
        self.path = self.cipher.path
    
    def tearDown(self):
        if os.path.exists(self.path / "test_key.key"):
            os.remove(self.path / "test_key.key")
        if os.path.exists(self.path / "test_text_file"):
            os.remove(self.path / "test_text_file")
        if os.path.exists(self.path / 'result.enc'):
            os.remove(self.path / 'result.enc')
        if os.path.exists(self.path / "decrypt_test_file.txt"):
            os.remove(self.path / "decrypt_test_file.txt")
        
    
    def testMainEncryptDecryptFile(self):
        """
        Test to make sure the whole prcosses of the main fucntion works as intended when running on the file input path of the script"""
        with open(self.path / 'test_text_file', 'w') as file:
            file.write("hello world")

        self.cipher.Main("encrypt", "file", 'test_text_file', "result.enc", self.key)

        with open(self.path / "test_text_file", 'rb') as file:
            test_input = file.read()
        
        self.cipher.Main("decrypt", "file", 'result.enc', "decrypt_test_file.txt", self.key)

        with open(self.path / "decrypt_test_file.txt", 'rb') as file:
            test_output = file.read()

        self.assertEqual(test_input, test_output)

    def testMainEncryptDecryptInput(self):
        """
        Test to make sure the whole prcosses of the main fucntion works as intended when running on the terminal input path of the script"""
        test_terminal_input = "hello world"

        self.cipher.Main("encrypt", "terminal_input", test_terminal_input, "result.enc", self.key)

        with open(self.path / "result.enc", 'rb') as file:
            encrypted_message = file.read()

        self.cipher.Main("decrypt", "terminal_input", encrypted_message, "decrypt_test_file.txt", self.key)

        with open(self.path / "decrypt_test_file.txt", 'r') as file:
            test_output = file.read()

        self.assertEqual(test_terminal_input, test_output)

    def test_get_key(self):
        """
        Test that get_key correctly loads and returns a Fernet encryption suite 
        when provided with a valid key file.
        """
        cipher_suite = self.cipher.get_key(self.key)
    
        self.assertIsInstance(cipher_suite, Fernet, "get_key should return a Fernet encryption suite")


        



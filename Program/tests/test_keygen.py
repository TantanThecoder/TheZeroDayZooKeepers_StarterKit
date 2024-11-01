from Cipher.keygen import Keygen
from cryptography.fernet import Fernet
import unittest
import os
from pathlib import Path


class TestKeygen(unittest.TestCase):

    def setUp(self):
        self.keygen = Keygen()
        self.path = self.keygen.path
        self.path.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.path / "test_key.key"):
            os.remove(self.path / "test_key.key")
        
    def test_generate_key(self):
        self.keygen.Main("test_key.key")

        test_key_path = self.path / "test_key.key"
        self.assertTrue(test_key_path.exists(), "Key file was not created.")

        with open(test_key_path, "rb") as key_file:
            key = key_file.read()
            try:
                Fernet(key)
            except ValueError:
                self.fail("The generated key is not valid.")

        
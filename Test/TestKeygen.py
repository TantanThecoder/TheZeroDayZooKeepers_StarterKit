# from cryptography.fernet import Fernet
# import unittest
# import os
# from Program.Cipher.keygen import Keygen


# class TestKeygen(unittest.TestCase):
#     def setUp(self) -> None:
#         self.keygen = Keygen()
#         self.test_key_file = "test_key_file"
    
#     def tearDown(self):
#         if os.path.exists(self.keygen.path / self.test_key_file):
#             os.remove(self.keygen.path / self.test_key_file)
        
#     def test_keyfile_exists(self):
#         self.keygen.Main(self.test_key_file)
#         self.assertTrue(os.path.exists(self.keygen.path / self.test_key_file))


# if __name__ == "__main__":
#     unittest.main()
        




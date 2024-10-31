# import unittest
# import os
# from cryptography.fernet import Fernet
# from Program.Cipher.cipher import Cipher

# class TestCipher(unittest.TestCase):

#     def setUp(self):
#         self.key = Fernet.generate_key()
#         self.cipher_suite = Fernet(self.key)
#         self.cipher = Cipher()

#         with open("test_key.key", "wb") as key_file:
#             key_file.write(self.key)

#     def tearDown(self):
#         if os.path.exists("test.enc"):
#             os.remove("test.enc")
#         if os.path.exists("output.txt"):
#             os.remove("output.txt")
#         if os.path.exists("decrypted_test.txt"):
#             os.remove("decrypted_test.txt")
#         if os.path.exists("test_key.key"):
#             os.remove("test_key.key")

#     def test_encrypt_text_input(self):
#         input_text = "Hello, World!"
#         self.cipher.Encrypt(self.cipher_suite, input_text, "test.enc", data_type="Text")
#         self.assertTrue(os.path.exists("test.enc"))

#     def test_encrypt_file_input(self):
#         with open("test_input.txt", 'w') as file:
#             file.write("Hello, testing encryption!")
        
#         self.cipher.Encrypt(self.cipher_suite, "test_input.txt", "test.enc", data_type="File")
#         self.assertTrue(os.path.exists("test.enc"))

#         os.remove("test_input.txt")

#     def test_decrypt_text_input(self):
#         input_text = "Secret message"
#         encrypted_text = self.cipher_suite.encrypt(input_text.encode())
        
#         with open("test.enc", "wb") as f:
#             f.write(encrypted_text)

#         self.cipher.Decrypt(self.cipher_suite, "test.enc", "decrypted_test.txt", data_type="File")

#         with open("decrypted_test.txt", "r") as f:
#             decrypted_text = f.read()
#         self.assertEqual(decrypted_text, input_text)
        
#     def test_decrypt_missing_file(self):
#         with self.assertLogs(level='ERROR') as log:
#             self.cipher.Decrypt(self.cipher_suite, "non_existing_file.enc", "output.txt", data_type="File")
#             self.assertIn("Could not find the specified file", log.output[0])

    
#     def test_invalid_key(self):
#         input_text = "Testing invalid key"
#         encrypted_text = self.cipher_suite.encrypt(input_text.encode())

#         with open("test.enc", 'wb') as file:
#             file.write(encrypted_text)

#         other_key = Fernet.generate_key()
#         other_cipher_suite = Fernet(other_key)
        
#         with self.assertRaises(Exception):
#             self.cipher.Decrypt(other_cipher_suite, "test.enc", "decrypted_test.txt", data_type="File")

        
#     def test_main_function(self):
#         input_text = "Encrypt and Decrypt using Main"
        
#         self.cipher.Main("Encrypt", "Text", input_text, "test.enc", "test_key.key")
#         self.assertTrue(os.path.exists("test.enc"))

#         self.cipher.Main("Decrypt", "File", "test.enc", "decrypted_test.txt", "test_key.key")
#         with open("decrypted_test.txt", "r") as f:
#             decrypted_text = f.read()
#         self.assertEqual(decrypted_text, input_text)

# if __name__ == "__main__":
#     unittest.main()

        
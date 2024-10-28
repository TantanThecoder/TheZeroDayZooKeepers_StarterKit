from Program.Scanner.scanner import Scanner

import os
import unittest
from unittest.mock import patch, MagicMock
import json



class TestScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = Scanner()
        self.test_file = "test_file.txt"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


    def test_write_file(self):
        message = "hello, world\n"
        self.scanner.write_file(message, self.test_file)

        with open(self.test_file, 'r') as file:
            result = file.read()
        
        self.assertEqual(message, result)
    
    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_write_file_file_not_found(self, mock_open):
        with self.assertLogs(level='ERROR') as log:
            self.scanner.write_file("test data", "invalid_path/test.txt")
            self.assertIn("Could not find the specified file", log.output[0])
    
    @patch('builtins.open', side_effect=PermissionError)
    def test_write_file_permission_error(self, mock_open):
        with self.assertLogs(level='ERROR') as log:
            self.scanner.write_file("test data", self.test_file)
            self.assertIn("Permission denied", log.output[0])
    

    def test_read_file(self): 
        expected_result = ["10.2.10.153", "10.2.10.154", "10.2.10.113", "even"]
        with open(self.test_file, 'w') as f:
            f.write("10.2.10.153\n10.2.10.154\n10.2.10.113\neven\n")
        result = self.scanner.read_file(self.test_file)

        self.assertEqual(expected_result, result)
    
    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_file_file_not_found(self, mock_open):
        with self.assertLogs(level='ERROR') as log:
            result = self.scanner.read_file("invalid_path.txt")
            self.assertIsNone(result)
            self.assertIn("Could not find the specified file", log.output[0])

    @patch('builtins.open', side_effect=PermissionError)
    def test_read_file_permission_error(self, mock_open):
        with self.assertLogs(level='ERROR') as log:
            result = self.scanner.read_file(self.test_file)
            self.assertIsNone(result)
            self.assertIn("Permission denied", log.output[0])

    def test_format_scan(self):
        sample_output = {
            "host": "192.168.1.1",
            "hostname": "example.com",
            "state": "up",
            "tcp": {
                "22": {"state": "open", "name": "ssh"},
                "80": {"state": "open", "name": "http"},
            }
        }
        expected_output = json.dumps(sample_output, indent=4)

        formated_result = self.scanner.format_scan(sample_output)

        self.assertEqual(formated_result, expected_output)



if __name__ == "__main__":
    unittest.main()


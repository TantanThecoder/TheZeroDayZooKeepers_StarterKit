try:
    from cryptography.fernet import Fernet
except ImportError:
    logging.error("Cryptography library missing! Please run 'pip install cryptography'")
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


class Keygen:
    def __init__(self):
        self.path = Path.cwd() / "Cipher" / "Cipher_files"
        self.path.mkdir(parents=True, exist_ok=True)

    def Main(self, file_name):
        """
        Generates a cryptographic key and saves it to the specified file.
        If no file is specified, 'generated.key' is used as default.
        """
        key = Fernet.generate_key()
        try:
            with open(self.path / file_name, "wb") as key_file:
                key_file.write(key)
        except Exception as e:
            logging.error(f"An unexcpected error occured: {e}")

        logging.info("A key has been saved!")



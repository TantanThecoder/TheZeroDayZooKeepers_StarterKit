from pathlib import Path
import logging
import re
import ipaddress

class Validator:

    @staticmethod
    def validate_ip(ip):
        """Checks that the given ip is a valid ip adress."""
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            logging.error(f" Invalid IP adress: {ip}")
            return False

    @staticmethod
    def validate_path(file_path):
        """Check that a given file path exists and is a valid path."""
        if Path(file_path).exists():
            return True
        logging.error(f" Invalid or non-existent file path: {file_path}")
        return False

    @staticmethod
    def validate_non_empty(value, name='Value'):
        """Generic non-empty check."""
        if value:
            return True
        logging.error(f" {name} cannot be empty.")
        return False

    @staticmethod
    def validate_domain(domain):
        """Checks that a given domain is a valid domain."""
        domain_regex = re.compile(
        r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.'
        r'[A-Za-z]{2,}$'
        )
        if domain_regex.match(domain):
            return True

        return False
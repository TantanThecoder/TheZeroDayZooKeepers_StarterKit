try:
    import sublist3r
except ImportError:
    logging.error("sublist3r library is not installed! Please run 'pip install sublist3r'.")
import requests
import logging
import json
from pathlib import Path


def load_config():
    file_path = "config.json"
    try:
        with open(file_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logging.error(f"The file config.json was not found!")

config = load_config()

class Enumeration:
    def __init__(self) -> None:
        pass

    def Main(self, domain, thread, savefile):
        """
        Performs subdomain enumeration on a given domain and writes the result to a file.
        Parameters:
        - domain: Target domain to enumerate subdomains.
        - thread: Number of threads for concurrent enumeration.
        - savefile: Output file to store the results.
        - ports: Optional port scanning (currently unused).
    """
        subdomains = sublist3r.main(domain, thread, savefile, ports=config.get("enumeration_port_option"), silent= config.get("enumeration_silent_option"), verbose= config.get("enumeration_verbose_option"), enable_bruteforce= config.get("enumeration_bruteforce_option"), engines= config.get("enumeration_engine_option"))

        with open(savefile, 'w') as file:
            for subdomain in subdomains:
                try:
                    response = requests.get(f"https://{subdomain}", timeout=5)
                    status = response.status_code    
                    file.write(f"Subdomain is up: {subdomain} : {status}\n")
                except requests.ConnectionError:
                    file.write(f"Subdomain is down: {subdomain}\n")
                except requests.Timeout:
                    file.write(f"Subdomain timeout: {subdomain}\n")
                except Exception as e:
                    logging.error(f"An error occured: {e}")

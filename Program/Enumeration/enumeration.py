try:
    import sublist3r
except ImportError:
    logging.error("sublist3r library is not installed! Please run 'pip install sublist3r'.")
import requests
import logging
from Validator.validator import Validator
from Json_config.json_config import Json_config
import sys

json_config = Json_config()
config = json_config.load_config()

if not config:
    logging.error("Configuration file 'config.json' is missing or invalid. Please create it with default settings or check github for correct file!")
    sys.exit("Exiting due to configuration error.")

class Enumeration:
    def __init__(self) -> None:
        pass

    def Main(self, domain, thread, savefile):
        """
        Performs subdomain enumeration on a given domain and writes the result to a file.
        
         Args:
            - domain: Target domain to enumerate subdomains.
            - thread: Number of threads for concurrent enumeration.
            - savefile: Output file to store the results.
            - ports: Optional port scanning (currently unused).
    """
        while True:
            if not Validator.validate_domain(domain):
                logging.warning(f"Invalid domain name: {domain}")
                domain = input("Input a new domain: ")
            else:
                break

            


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

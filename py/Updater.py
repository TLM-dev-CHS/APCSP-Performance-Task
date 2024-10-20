from py.Global import *
import requests
from colorama import Fore, Style
from packaging.version import parse

ONLINE_VERSION = requests.get(f"{BASE_URL}/txt/version.txt").text

class Updater:
    def __init__(self):
        logging.info("Checking for updates...")
        self.VersionChecker()
        
    def VersionChecker(self):
        LV = parse(ONLINE_VERSION)
        CV = parse(VERSION)
        
        logging.info(f"Local version: {VERSION}")
        logging.info(f"Online version: {ONLINE_VERSION}")
        
        if CV < LV:
            logging.info(f"{Fore.YELLOW}Update available!{Style.RESET_ALL}")
            Q = InputSyntax("Would you like to update?", ["Yes", "No"])
            if Q == "Yes":
                logging.info("Updating...")
            elif Q == "No":
                logging.info("Update has been cancelled!")
        elif CV == LV:
            logging.info(f"{Fore.GREEN}You are up to date!{Style.RESET_ALL}")
        else:
            logging.error(f"{Fore.RED}Invalid version numbers!{Style.RESET_ALL}")
            logging.info("Please contact the developer to fix this issue...")
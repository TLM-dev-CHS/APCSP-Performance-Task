import os
import logging
import datetime
from colorama import Fore, Style

CURRENT_DIR = os.getcwd()
APP_NAME = "App Frame"
BASE_URL = "https://raw.githubusercontent.com/TLM-dev-CHS/APCSP-Performance-Task/refs/heads/main"

VERSION = "1.0.0"

DATE_STR = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] - [%(levelname)s] - [%(name)s] - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(CURRENT_DIR, "logs", f"[{DATE_STR}] {APP_NAME}.log")),
        logging.StreamHandler()
    ]
)

def InputSyntax(message, choices):
    TEMP_CHOICES = ", ".join(choices)  
    
    while True:       
        question = input(f"{message}\n\nOptions are: ({TEMP_CHOICES})\n\n>>> ")
        if question in choices:
            return question
        else:
            logging.error(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")
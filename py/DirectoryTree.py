import os
import requests
from colorama import Fore, Style

from py.Global import *

hierarchy = {
    "ini": {
        "credits.ini"
    },
    "json": {
        "settings.json"
    },
    "logs": None,
    "tmp": None,
    "jpg": None
}

files = []
folders = []
links = []

for folderItem, fileItems in hierarchy.items():
    folderPath = os.path.join(CURRENT_DIR, folderItem)
    folders.append(folderPath)
    if fileItems:
        for fileItem in fileItems:
            filePath = os.path.join(folderPath, fileItem)
            files.append(filePath)
            
            linkItem = f"{BASE_URL}/{folderItem}/{fileItem}"
            links.append(linkItem)

class FolderCreation:
    def __init__(self):
        logging.info("Checking folder structure...")
        logging.info("Creating folders...")
        self.FolderStructure()
        logging.info("Creating files...")
        self.FileStructure()
        logging.info(f"{Fore.GREEN}Folders and files created successfully!{Style.RESET_ALL}")
    
    def FolderStructure(self):
        for folder in folders:
            if not os.path.exists(folder):
                os.makedirs(folder)
                logging.info(f"{Fore.GREEN}Your folder at {repr(folder)} has been created!{Style.RESET_ALL}")
            else:
                logging.info(f"{Fore.YELLOW}Your folder at {repr(folder)} already exists...{Style.RESET_ALL}")
            
        logging.info(f"{Fore.GREEN}Folders created successfully!{Style.RESET_ALL}")
    
    def FileStructure(self):
        for file in files:
            data = requests.get(links[files.index(file)]).text
            
            try:
                with open(file, 'r') as r:
                    localContent = r.read()
            except FileNotFoundError:
                localContent = ""
                logging.error(f"{Fore.RED}File does not exist at {repr(file)}!{Style.RESET_ALL}")
            
            if localContent != data:
                logging.info(f"Writing data to {repr(file)}...")
                with open(file, 'w') as w:
                    w.write(data)
                logging.info(f"{Fore.GREEN}Successfully wrote data to {repr(file)}!{Style.RESET_ALL}")
            
            else:
                logging.info(f"{Fore.YELLOW}Content in {repr(file)} is already up to date...{Style.RESET_ALL}")
            
        logging.info(f"{Fore.GREEN}Files created successfully!{Style.RESET_ALL}")
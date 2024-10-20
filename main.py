import customtkinter as ctk
from colorama import Fore, Style

from py.Global import *
from py.DirectoryTree import *
from py.Updater import *


class App(ctk.CTk):
    def __init__(self):
        logging.info("Initializing the app...")
        self.InternetCheck()
    
    def InternetCheck(self):
        logging.info("Checking internet connection...")
        try:
            logging.info(f"{Fore.GREEN}Internet connection detected!{Style.RESET_ALL}")
            self.Prerequesties()
        except ConnectionError:
            logging.error(f"{Fore.RED}No internet connection!{Style.RESET_ALL}")
        
    def Prerequesties(self):
        FolderCreation()
        Updater()
        logging.info(f"{Fore.GREEN}Prerequesties checked successfully!{Style.RESET_ALL}")
        self.AppStructure()
        
    def AppStructure(self):
        super().__init__()
        
        self.title(F"{APP_NAME}, v{VERSION}")
        self.minsize(1000, 800)
        self.resizable(False, False)
        
        self.mainloop()
        
App()
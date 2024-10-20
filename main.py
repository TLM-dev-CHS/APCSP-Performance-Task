import customtkinter as ctk
from colorama import Fore, Style

from py.Global import *
from py.DirectoryTree import *
from py.Updater import *


class App(ctk.CTk):
    def __init__(self):
        logging.info("Initializing launch procedures...")
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
        logging.info("Starting the GUI...")
        self.AppStructure()
        
    def AppStructure(self):
        super().__init__()
        
        logging.info(f"{Fore.GREEN}GUI started successfully!{Style.RESET_ALL}")
        
        self.title(F"{APP_NAME}, v{VERSION}")
        self.minsize(1000, 800)
        self.resizable(False, False)
        
        self.TopFrame()
        self.ContentFrame()
        
        self.mainloop()
    
    def TopFrame(self):
        topFrame = ctk.CTkFrame(master=self)
        topFrame.pack(pady=(20,0), padx=20, fill="both")
        
        title = ctk.CTkLabel(master=topFrame, text=f"Welcome to {APP_NAME}!", font=("Segoe UI", 36, "bold"))
        title.pack(side="left", padx=20, pady=20)
        
    def ContentFrame(self):
        contentFrame = ctk.CTkFrame(master=self)
        contentFrame.pack(pady=20, padx=20, fill="both", expand=True)
        
        title = ctk.CTkLabel(master=contentFrame, text=1, font=("Segoe UI", 36, "bold"))
        title.pack(side="left", padx=20, pady=20)
            
App()
from utils.PathHandler import *
from utils.Global import *
from utils.Settings import * 
from utils.Updater import *
from utils.Credits import *
from colorama import Fore, Style

class App(ctk.CTk):
    def __init__(self):
        self.SETTINGS = Settings()
        ctk.set_default_color_theme(self.SETTINGS.COLOR_SCHEME)
        self.launcherProcesses()
        self.App()

    def launcherProcesses(self):
        # FileStructure()
        
        # Access AUTO_UPDATE through self.SETTINGS
        if self.SETTINGS.AUTO_UPDATE == "True": 
            logging.info(f"{Fore.GREEN}Automatic updating is turned on.{Style.RESET_ALL}")
        else:
            logging.info(f"{Fore.RED}Automatic updating is turned off.{Style.RESET_ALL}")

    def App(self):
        super().__init__()
        
        self.title(APP_NAME)
        self.minsize(900,500)
        self.resizable(False, False)
        
        self.topFrame = ctk.CTkFrame(master=self)
        self.topFrame.pack(fill="both", expand=False, padx=15, pady=(15,0))
        
        self.contentFrame = ctk.CTkScrollableFrame(master=self)
        self.contentFrame.pack(fill="both", expand=True, padx=15, pady=15)

        self.TopFrame()
        self.ContentFrame()
        
        self.mainloop()
        
    # --- topFrame Contents ---
    def TopFrame(self):
        self.titleLabel = ctk.CTkLabel(master=self.topFrame, text=f"Welcome to {APP_NAME}!", font=(self.SETTINGS.FONT_TYPE, 24, "bold"))
        self.titleLabel.pack(side="left", padx=15, pady=15, ipadx=5, ipady=5)
        
        self.settingsButton = ctk.CTkButton(master=self.topFrame, text="Settings", font=(self.SETTINGS.FONT_TYPE, 16), command=self.OPEN_SETTINGS)
        self.settingsButton.pack(side="right", padx=(0,15), pady=15, ipadx=5, ipady=5)        

        self.creditsButton = ctk.CTkButton(master=self.topFrame, text="Credits", font=(self.SETTINGS.FONT_TYPE, 16), command=self.OPEN_CREDITS)
        self.creditsButton.pack(side="right", padx=7.5, pady=15, ipadx=5, ipady=5)
        
    def ContentFrame(self):
        pass
    
    def OPEN_SETTINGS(self):
        SettingsApp().mainloop()
        
    def OPEN_CREDITS(self):
        CreditsMenu().mainloop()
        
App()  # Create an instance of Launcher to run its processes

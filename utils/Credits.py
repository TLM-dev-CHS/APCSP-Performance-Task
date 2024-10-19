from utils.Global import *
from utils.Settings import *
import customtkinter as ctk

config.read(os.path.join(CURRENT_DIR, "ini", "credits.ini"))

class CreditsMenu(ctk.CTk):
    def __init__(self):
        Settings.loadSettings(self=self)
        self.SETTINGS = Settings()
        
        ctk.set_default_color_theme(self.SETTINGS.COLOR_SCHEME)
        self.appFrame()
    
    def appFrame(self):
        super().__init__()
        
        self.title("Credits")
        self.minsize(400,500)
        self.resizable(False, False)
        
        self.createWidgets()
        
    def createWidgets(self):
        self.mainTitleLabel = ctk.CTkLabel(master=self, 
                                      text="Credits:", 
                                      font=(self.SETTINGS.FONT_TYPE, 36)) 
        self.mainTitleLabel.pack(anchor=self.SETTINGS.ANCHOR_VALUE, padx=20, pady=(20, 10)) 
                
        self.mainFrame = ctk.CTkScrollableFrame(master=self)
        self.mainFrame.pack(fill="both", expand=True, padx=15, pady=10)
        
        for section in config.sections():
            self.sectionFrame = ctk.CTkFrame(master=self.mainFrame)
            self.sectionFrame.pack(fill="both", expand=True, pady=10)
            
            self.sectionTitle = ctk.CTkLabel(master=self.sectionFrame, text=section, font=(self.SETTINGS.FONT_TYPE, 24, "bold"))
            self.sectionTitle.pack(anchor="w", padx=20, pady=(5, 5))  # Adjusted pady
            
            for key, value in config[section].items():
                self.keyFrame = ctk.CTkFrame(master=self.sectionFrame)
                self.keyFrame.pack(fill="both", expand=True, padx=20, pady=(5, 5))  # Adjusted padx, pady
                
                self.keyLabel = ctk.CTkLabel(master=self.keyFrame, text=f"{key.capitalize()}:", font=(self.SETTINGS.FONT_TYPE, 18))
                self.keyLabel.pack(anchor=self.SETTINGS.ANCHOR_VALUE, padx=5, pady=5)  # Adjusted padx, pady

                self.valueLabel = ctk.CTkLabel(master=self.keyFrame, text=f"{value}", font=(self.SETTINGS.FONT_TYPE, 14), wraplength=300)
                self.valueLabel.pack(anchor=self.SETTINGS.ANCHOR_VALUE, padx=5, pady=5)  # Adjusted padx, pady

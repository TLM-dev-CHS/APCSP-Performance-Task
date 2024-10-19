# Online Packages
import customtkinter as ctk  # Import the customtkinter module for creating GUI elements
import json  # Import the json module for working with JSON data
import logging # Import the logging module for logging messages
from colorama import Fore, Style

# Local Imports
from utils.Global import *  # Import global variables and functions from the Global module

# Declare the SettingsApp class
class SettingsApp(ctk.CTk):   
    """
    A class to create and manage the settings application window.
    """
    def __init__(self):
        self.SETTINGS = Settings()
        """
        Initializes the SettingsApp class.
        Loads settings, sets the default color theme, and creates the application structure and widgets.
        """
        with open(SETTINGS_PATH, 'r') as f:
            self.JSON_DATA = json.load(f) 
                   
        Settings.loadSettings(self)
        logging.info("Initializing SettingsApp")
        ctk.set_default_color_theme(self.SETTINGS.COLOR_SCHEME)  # Set the default color theme based on loaded settings
        self.appStructure()  # Create the basic structure of the application window
        self.createWidgets()  # Create and populate the widgets within the application window
        logging.info("SettingsApp initialized successfully")

    def appStructure(self):
        """
        Creates the basic structure of the application window, including the title, size, and main widgets.
        """
        logging.info("Creating application structure")
        super().__init__()  # Initialize the parent class (ctk.CTk)
        
        self.title(f"{APP_NAME} | Settings")  # Set the title of the window
        self.minsize(400,700)  # Set the minimum size of the window
        self.resizable(False, False)  # Make the window non-resizable

        # Create the main title label and pack it into the window
        self.mainTitleLabel = ctk.CTkLabel(master=self, 
                                      text="Settings:", 
                                      font=(self.SETTINGS.FONT_TYPE, 36)) 
        self.mainTitleLabel.pack(anchor=self.SETTINGS.ANCHOR_VALUE, padx=20, pady=(20, 10))  # Adjusted pady
        
        # Create a scrollable frame to hold the content and pack it into the window
        self.mainFrame = ctk.CTkScrollableFrame(self)
        self.mainFrame.pack(padx=15, pady=10, fill="both", expand=True)  # Adjusted pady
        
        # Create a tabview widget to organize settings into different sections
        self.tabFrame = ctk.CTkTabview(master=self.mainFrame)
        self.tabFrame.pack(fill="both", expand=True)
        logging.info("Application structure created successfully")
        
    def createWidgets(self):
        """
        Creates and populates the widgets within the application window based on the loaded settings.
        Iterates through the settings data, creating tabs, sections, labels, and comboboxes as needed.
        """
        logging.info("Creating widgets")
        # Iterate through each section in the settings
        for sectionName, sectionData in self.JSON_DATA.items():
            logging.debug(f"Creating tab for section: {sectionName}")
            self.tabFrame.add(sectionName)  # Add a new tab for the current section
            
            # Create a frame to hold the content of the current section
            frame = ctk.CTkFrame(master=self.tabFrame.tab(sectionName))
            frame.pack(fill="both", expand=True)
            
            # Iterate through each key-value pair within the current section
            for key, entry in sectionData.items():
                logging.debug(f"Creating widgets for key: {key}")
                # Create a frame for the current key's options
                sectionFrame = ctk.CTkFrame(master=frame, width=400)
                sectionFrame.pack(fill="both", expand=True, pady=10)  # Adjusted pady
                
                # Create a label for the current key's options and pack it into the frame
                label = ctk.CTkLabel(master=sectionFrame, 
                                     text=f"{key} Options:", 
                                     font=(self.SETTINGS.FONT_TYPE, 24, "bold"))
                label.pack(anchor=self.SETTINGS.ANCHOR_VALUE, padx=20, pady=(5, 5))  # Adjusted pady

                # Iterate through each entry within the current key's options
                for entryName, entryData in entry.items():
                    logging.debug(f"Creating widgets for entry: {entryName}")
                    # Create a frame for the current entry
                    entryFrame = ctk.CTkFrame(master=sectionFrame, width=400)
                    entryFrame.pack(anchor='ce', padx=20, pady=(5,5))  # Adjusted padx, pady
                    
                    # Create a label for the current entry's name and pack it into the frame
                    nameLabel = ctk.CTkLabel(master=entryFrame, 
                                        text=f"{entryName}:",
                                        font=(self.SETTINGS.FONT_TYPE, 18),
                                        justify=self.SETTINGS.JUSTIFY_VALUE,
                                        anchor=self.SETTINGS.ANCHOR_VALUE,
                                        width=400)
                    nameLabel.pack(anchor=self.SETTINGS.ANCHOR_VALUE, padx=15, pady=(10, 10), expand=True)  # Adjusted padx, pady
                    
                    # Check if the current entry has data
                    if isinstance(entryData, dict):
                        # Iterate through each data key-value pair within the current entry
                        for dataKey, dataValue in entryData.items():                    
                            # If the data key is "information", create an information label
                            if dataKey == "information":
                                logging.debug(f"Creating information label for: {dataValue}")
                                infoLabel = ctk.CTkLabel(master=nameLabel,
                                                    text=f"- {dataValue}", 
                                                    font=(self.SETTINGS.FONT_TYPE, 12),
                                                    justify=self.SETTINGS.JUSTIFY_VALUE,
                                                    anchor=self.SETTINGS.ANCHOR_VALUE,
                                                    wraplength=200)
                                infoLabel.grid(row=1, column=0, sticky=self.SETTINGS.STICKY_VALUE, padx=5, pady=5)  # Adjusted padx, pady
                            
                            # If the data key is "value", create a string variable to store the value
                            elif dataKey == "value":
                                logging.debug(f"Creating string variable for: {dataKey}")
                                optionsTemp = self.JSON_DATA[sectionName][key][entryName][dataKey]
                                self.variableData = ctk.StringVar(value=optionsTemp)
                                                                                            
                            # If the data key is "options", create a combobox widget
                            elif dataKey == "options":
                                logging.debug(f"Creating combobox widget for: {dataKey}")
                                optionsHeader = self.JSON_DATA[sectionName][key][entryName][dataKey]
                                self.dataKey = dataKey
                                
                                # Determine the options for the combobox based on the options header
                                if optionsHeader == "bool":
                                    options = ["True", "False"]
                                elif optionsHeader == "int":
                                    options = [str(i) for i in range(1,11)]
                                else:
                                    options = optionsHeader
                                
                                # Create the combobox widget and configure its settings
                                comboBoxWidget = ctk.CTkComboBox(master=nameLabel, 
                                                        values=options, 
                                                        font=(self.SETTINGS.FONT_TYPE, 12),
                                                        justify=self.SETTINGS.JUSTIFY_VALUE,
                                                        variable=self.variableData)

                                # Store the entry name and data key as attributes of the widget
                                comboBoxWidget.entryName = entryName
                                comboBoxWidget.dataKey = dataKey 
                                # Set the command to be executed when the combobox selection changes
                                comboBoxWidget.configure(command=lambda choice, w=comboBoxWidget: self.recordChoices(choice, w))
                                # Place the widget in the grid layout
                                comboBoxWidget.grid(row=2, column=0, sticky=self.SETTINGS.STICKY_VALUE, padx=5, pady=5)  # Adjusted padx, pady   
        logging.info("Widgets created successfully")
                                
    def recordChoices(self, choice, comboBoxWidget):
        """
        Records the user's choice from a combobox widget and updates the settings.json file.
        """
        if choice == self.variableData:
            logging.warning(f"{Fore.RED}Your choice is already stored in the settings file...{Style.RESET_ALL}")
        else:
            logging.info(f"{Fore.YELLOW}Recording choice: {choice}{Style.RESET_ALL}")
            # Get the active tab name, key, and entry name from the widget
            sectionName = self.tabFrame.get()
            key = list(self.JSON_DATA[sectionName].keys())[0]
            entryName = comboBoxWidget.entryName
            
            # Update the value in the settings dictionary
            self.JSON_DATA[sectionName][key][entryName]["value"] = choice

            # Write the updated settings dictionary back to the settings.json file
            with open(SETTINGS_PATH, "w") as w:
                json.dump(self.JSON_DATA, w, indent=4)  # Use indent for pretty formatting
            logging.info(f"{Fore.GREEN}Choice recorded successfully{Style.RESET_ALL}")

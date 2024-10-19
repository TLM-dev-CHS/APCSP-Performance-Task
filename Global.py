"""
This module defines global variables and functions used across the application.
"""

# --- Online Imports ---
import os
import configparser
import customtkinter as ctk
import logging
import json

# --- Local Imports
from utils import PathHandler

# --- Constants ---
TEMPLATE_URL = "https://raw.githubusercontent.com/TLM-dev-CHS/APCSP-Performance-Task/refs/heads/main/"
CURRENT_DIR = os.getcwd()
APP_NAME = "App Frame"
SETTINGS_PATH = os.path.join(CURRENT_DIR, "json", "settings.json")

# --- Global Initialization ---
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - [%(levelname)s] - %(message)s')
config = configparser.ConfigParser()

# --- Default Settings --- #
class Settings:
    def __init__(self):
        self.loadSettings()

    def loadSettings(self):
        try:
            with open(SETTINGS_PATH, "r") as r:
                settingsData = json.load(r)

            # General Settings
            self.AUTO_UPDATE = settingsData["General"]["Launcher"]["Auto-Update"]["value"]
            
            # Theme Settings
            self.COLOR_SCHEME = settingsData["Appearance"]["Theme"]["Color Scheme"]["value"]
            self.JUSTIFY_VALUE = settingsData["Appearance"]["Theme"]["Alignment"]["value"]
            self.LIGHT_DARK_MODE = settingsData["Appearance"]["Theme"]["Light/Dark Mode"]["value"]

            # Font Settings
            self.FONT_TYPE = settingsData["Appearance"]["Font"]["Type"]["value"]
            self.FONT_SIZE = settingsData["Appearance"]["Font"]["Size"]["value"]
            self.FONT_WEIGHT = settingsData["Appearance"]["Font"]["Weight"]["value"]

            # Scaling Settings
            self.HIGH_DPI_AWARENESS = settingsData["Appearance"]["Scaling"]["High DPI Awareness"]["value"]
            self.GLOBAL_SCALE = settingsData["Appearance"]["Scaling"]["Global Scale"]["value"]
            self.CORNER_RADIUS = settingsData["Appearance"]["Scaling"]["Corner Radius"]["value"]

            # Alignment Settings
            self.ALIGNMENT = settingsData["Appearance"]["Theme"]["Alignment"]["value"]
            
            if self.ALIGNMENT == "left":
                self.ANCHOR_VALUE = "w"
                self.STICKY_VALUE = "w"
            elif self.ALIGNMENT == "center":
                self.ANCHOR_VALUE = "center"
                self.STICKY_VALUE = "ew"
            elif self.ALIGNMENT == "right":
                self.ANCHOR_VALUE = "e"
                self.STICKY_VALUE = "e"
            
        except FileNotFoundError:
            print(f"Settings file not found at: {SETTINGS_PATH}")
        except json.JSONDecodeError:
            print(f"Invalid JSON format in: {SETTINGS_PATH}")
        except KeyError as e:
            print(f"Missing key in settings file: {e}")

# --- Utility Functions ---
def inputSyntax(self, message, options: list):
    """Prompts the user for input with a list of valid options."""
    list_options = "\n".join(options)
    while True:
        choice = input(f"{message}\n\nOptions:\n{list_options}\n\n>>> ")
        if choice in options:
            return choice
        else:
            logging.warning(f"Invalid option entered: {choice}\n\nPlease try again with another option...")
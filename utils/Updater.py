"""
This module defines the Updater class, checking for updates as a prerequistie for the application.
"""

# Online Packages
import logging
import os
import requests

# Global Imports
from utils.Global import *

# Define the Updater class
class Updater:        
    # Define the constructor for the Updater class
    def __init__(self):
        # Get the local and latest versions of the application
        self.localVersion = self.getVersions("local")
        self.latestVersion = self.getVersions("online")
        # Check if an update is available
        Updater.versionChecker(self)
    
    # Define the getVersions method, which retrieves the version of the application from a specified source
    def getVersions(self, source: str):
        # If the source is "local", get the version from the local credits.ini file
        if source == "local":
            filePath = os.path.join(CURRENT_DIR, "ini", "credits.ini")
        
        # If the source is "online", get the version from the remote credits.ini file
        elif source == "online":
            filePath = os.path.join(CURRENT_DIR, "tmp", "credits.ini")
            onlineURL = f"{TEMPLATE_URL}ini/credits.ini"
            
            # Download the contents of the remote credits.ini file
            response = requests.get(onlineURL).text
            
            # Write the contents of the remote credits.ini file to a local file
            with open(filePath, "w") as w:
                w.write(response)
        
        # If the source is invalid, log an error message and return None
        else: 
            logging.error(f"Invalid source specifiec: {repr(source)}")
            return None
            
        # Read the version from the specified credits.ini file
        config.read(filePath)
        version = config["Project Information"]["Version"]
        # Log the version that was read
        logging.info(f"The {'local' if source == 'local' else 'online'} version is {version}.")
        # Return the version that was read
        return version
    
    # Define the versionChecker method, which checks if an update is available and prompts the user to update if one is
    def versionChecker(self):
        # Get the local and latest versions of the application
        oldVersion = int(self.localVersion.replace(".", ""))
        newVersion = int(self.latestVersion.replace(".", ""))
        
        # If the local version is equal to the latest version, log a message indicating that no update is required
        if oldVersion == newVersion:
            logging.info("No update is required")
        
        # If the local version is less than the latest version, prompt the user to update
        elif oldVersion < newVersion:
            logging.info("An update is available...")
            confirm = inputSyntax("Would you like to update?", ["Yes", "No"])
            
            # If the user confirms the update, call the updateProcess method
            if confirm == "Yes":
                self.updateProcess()
                
            # If the user cancels the update, log a message indicating that the update has been canceled
            elif confirm == "No":
                logging.info("Update has been canceled, have a good day!")
    
    # Define the updateProcess method, which downloads the latest version of the application from GitHub
    def updateProcess(self):
        # Construct the URL to the latest version of the application on GitHub
        downloadURL = f"https://github.com/TLM-dev-CHS/APCSP-Performance-Task/archive/refs/tags/{self.latestVersion}.zip"
        
        # Attempt to download the latest version of the application from GitHub
        try:
            response = requests.get(downloadURL)
            response.raise_for_status()  # Check for HTTP errors

            # Save the downloaded file to the current working directory
            with open(f"APCSP-Performance-Task-{self.latestVersion}.zip", 'wb') as f:
                f.write(response.content)

            # Log a message indicating that the update was downloaded successfully
            logging.info(f"Successfully downloaded update to APCSP-Performance-Task-{self.latestVersion}.zip")

            os.remove(os.path.join(CURRENT_DIR, "tmp", "credits.ini"))

        # If an error occurs during the download process, log an error message
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading update: {e}")

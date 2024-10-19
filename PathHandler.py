"""
This module defines the FileStructure class, which is responsible for creating the folder structure file contents as a prerequistie for the application.
"""
# Online Packages
import os
import logging
import requests
import shutil

# Local Imports
from utils.Global import *
from utils.PathHandler import *

# Import Declarations
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - [%(levelname)s] - %(message)s')

# Define class variables for the current directory and the file hierarchy
hierarchy = {
        "ini": [
            "credits.ini"
            ],
        "json": [
            "settings.json"
            ],
        "logs": None,
        "tmp": None
    }

"""
Using a list here makes it easy to manage the files 
associated with each folder. If we need to add or 
remove files in the future, we only need to modify 
the list, not the logic of the loop.
"""

# Define the FileStructure class
class FileStructure:
    """
    Manages the creation of the application's folder structure and downloads necessary files.
    """
    def __init__(self):
        """
        Initializes the FileStructure class and starts the folder structure creation process.
        """
        # Log a message indicating that the folder structure is being created
        logging.info("Attempting to create folder structure, please wait...")
        
        # Call the createHierarchy method to create the folder structure and file content
        self.createHierarchy()  # Note: You don't need to call this with FileStructure.createHierarchy(self)
        
        # Log a message indicating that the folder structure has been created
        logging.info("Folder structure created!")
        
    # Define the createHierarchy method, which creates the folder structure for the application
    def createHierarchy(self):        
        """
        Creates the folder structure based on the defined hierarchy and downloads files from GitHub.
        
        This method iterates through the 'hierarchy' dictionary, where keys represent folder names 
        and values are lists of files to be created within those folders. 
        """
        # Iterate over the folders and files in the hierarchy dictionary
        for folder, files in hierarchy.items():
            # Construct the full path to the folder
            folderPath = os.path.join(CURRENT_DIR, folder)
            
            # If the folder doesn't exist, create it
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)
                logging.info(f"Created folder at {folder}!")
            
            # If the folder has files associated with it (files list is not empty), create them
            if files:
                # Iterate over the files in the folder
                for file in files:
                    # Construct the full path to the file
                    filePath = os.path.join(CURRENT_DIR, folder, file)

                    # If the file doesn't exist, create it
                    if not os.path.exists(filePath):
                        # Construct the URL to the raw file on GitHub
                        linkSuffix = f"{TEMPLATE_URL}{folder}/{file}"                     
                        # Download the content of the file from GitHub
                        data = requests.get(linkSuffix).text
                        
                        # Write the content of the file to the local file system
                        with open(filePath, 'w') as w:
                            w.write(data)

                        # Log a message indicating that the file has been appended
                        logging.info(f"Appended file at {filePath}!")
                    # If the file already exists, log a message indicating that
                    else:
                        logging.info(f"File already exists at {filePath}...")
            # If the folder doesn't have any files associated with it, log a message indicating that
            else:
                logging.info(f"No files to create for {folder}...")

# Define the ClearCache class
class ClearCache:
    """
    Manages the process of clearing the application's cache, 
    prompting the user for confirmation and optionally redownloading files.
    """
    def __init__(self):
        """
        Initializes the ClearCache class. 
        Sets up a flag to track if folders were deleted and starts the cache removal process.
        """
        self.foldersDeleted = False  # Flag to track if any cache folders were deleted

        logging.info("Starting the cache removal process...")
        self.confirmCacheDelete()  # Start the process by asking for user confirmation

    def confirmCacheDelete(self):
        """
        Prompts the user to confirm if they want to delete the cache.
        If confirmed, initiates the cache deletion process.
        """
        confirm = inputSyntax(f"Would you like to delete {self.APP_NAME}'s cache?", ["Yes", "No"])

        if confirm == "Yes":
            logging.info("Starting the deletion process...")
            self.removeCache()
        elif confirm == "No":
            logging.info("Cache deletion process has been canceled, have a good day!")

    def removeCache(self):
        """
        Iterates through the defined file hierarchy and removes cache folders.
        After deletion, prompts the user if they want to redownload missing files.
        """
        for folder, _ in hierarchy.items():
            folderPath = os.path.join(CURRENT_DIR, folder)
            if os.path.exists(folderPath):
                shutil.rmtree(folderPath)  # Delete the folder and its contents
                logging.info(f"The folder {repr(folder)} has been deleted.")
                self.foldersDeleted = True  # Mark that a folder was deleted
            else:
                logging.info(f"The folder {repr(folder)} does not exist.")

        # Inform the user about the cache status based on whether folders were deleted
        logging.info("The cache is now empty!") if self.foldersDeleted else logging.info("The cache is already empty...")

        # Ask if the user wants to redownload files after cache deletion
        confirm = inputSyntax("Would you like to redownload missing files?", ["Yes", "No"])

        if confirm == "Yes":
            logging.info("Starting the redownload process...")
            FileStructure()  # Assuming FileStructure handles file redownloading
        elif confirm == "No":
            logging.info("Redownload process has been canceled, have a good day!")

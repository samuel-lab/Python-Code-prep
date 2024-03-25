import tkinter as tk
from tkinter import filedialog
import json
import logging

def configure_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def open_folder_manager():
    logging.info("Opening folder manager dialog...")
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Open the folder manager dialog
    folder_path = filedialog.askdirectory()
    logging.info(f"Selected folder: {folder_path}")
    
    return folder_path

def save_folder_path(folder_path):
    logging.info("Saving folder path to config.json...")
    # Load existing data from config.json
    with open('data/config.json', 'r') as json_file:
        data = json.load(json_file)
    
    # Update the data dictionary with the folder path
    data["folder_path"] = folder_path
    
    # Save the updated data back to config.json
    with open('data/config.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logging.info("Folder path saved to data/config.json")

if __name__ == "__main__":
    configure_logging('data/app.log')
    logging.info("Starting script...")
    
    folder_path = open_folder_manager()
    if folder_path:
        save_folder_path(folder_path)
    else:
        logging.info("No folder selected.")

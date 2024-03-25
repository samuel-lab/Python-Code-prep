import json
import logging

def configure_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_input():
    logging.info("Collecting user input...")
    name = input("What is the name of your project?: ")
    logging.info(f"Project name entered: {name}")

    # Create a dictionary with the collected data
    data = {
        "name": name,
    }
    
    # Save the data to config.json
    with open('data/config.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logging.info("Configuration saved to data/config.json")

if __name__ == "__main__":
    configure_logging('data/app.log')
    logging.info("Starting script...")
    
    get_user_input()

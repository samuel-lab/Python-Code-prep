import os
import json
import subprocess
import logging


def configure_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def run_script(script_path):
    logging.info(f"Running script: {script_path}")
    subprocess.run(['python3', script_path], check=True)

def create_structure(name, folder_path):
    logging.info("Creating project structure...")
    # Create main directory
    main_dir = os.path.join(folder_path, name)
    os.makedirs(main_dir)
    logging.info(f"Created main directory: {main_dir}")

    # Create subdirectories
    subdirs = ['src/module1', 'tests', 'data', 'debug']
    for subdir in subdirs:
        subdir_path = os.path.join(main_dir, subdir)
        os.makedirs(subdir_path)
        logging.info(f"Created directory: {subdir_path}")

    # Create files
    files = {
        'src/module1/__init__.py': '',
        'src/module1/file1.py': '',
        'tests/test_module1.py': '',
        'data/index.html': '',
        'data/conf.py': '',
        'data/conf.json': '',
        'data/note.txt': '',
        'debug/app.log': '',      
        'main.py': '',
        'requirements.txt': '',
        'README.md': '',
        'Makefile': '',
        '.gitignore': '',
    }
    for filename, content in files.items():
        file_path = os.path.join(main_dir, filename)
        with open(file_path, 'w') as f:
            f.write(content)
        logging.info(f"Created file: {file_path}")

    # Create virtual environment
    venv_path = os.path.join(main_dir, 'venv')
    logging.info("Setting up virtual environment...")
    subprocess.run(['python3', '-m', 'venv', venv_path], check=True)
    logging.info(f"Virtual environment created at: {venv_path}")

def check_files_created(name, folder_path):
    logging.info("Checking if all files were created...")
    main_dir = os.path.join(folder_path, name)
    for root, dirs, files in os.walk(main_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.exists(file_path):
                logging.error(f"File not created: {file_path}")
            else:
                logging.info(f"File created: {file_path}")
    logging.info("File creation check complete.")

def main():
    configure_logging('data/app.log')
    logging.info("Starting script...")
    
    # Run settings.py
    run_script('src/settings.py')
    
    # Run path.py
    run_script('src/path.py')
    
    # Get project details from config.json
    with open('data/config.json') as config_file:
        config = json.load(config_file)
        name = config["name"]
        folder_path = config["folder_path"]
        create_structure(name, folder_path)
        logging.info(f"Project structure created in '{os.path.join(folder_path, name)}'")
    
    # Check if all files were created
    check_files_created(name, folder_path)

if __name__ == "__main__":
    main()

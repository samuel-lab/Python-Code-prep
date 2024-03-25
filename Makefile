# Makefile

# Virtual environment
venv:
	python -m venv venv

# Install dependencies
install:
	pip install -r requirements.txt

# Run the script to collect user input
get_user_input:
	python get_user_input.py

# Run the script to open folder manager
open_folder_manager:
	python open_folder_manager.py

# Run the main script to create project structure
create_structure:
	python main.py

# Clean up compiled files and directories
clean:
	rm -rf __pycache__/
	rm -rf venv/

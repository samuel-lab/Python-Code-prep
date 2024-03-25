# Project Python Code Prep

## Description
This project is designed to create a predefined directory structure and files for a Python project. It collects user input from a configuration file and uses it to create the project structure. Additionally, it runs scripts to set up project settings and paths.

## Usage
1. **For Windows:**
    Run `start.bat`

2. **For Mac OS and Linux:**
    Run `start.sh`

3. Type the name of your project in the command line.

4. Select the path where you want to create your project.

5. Wait until the project file is created.

## File Structure
Upon running the script, the following file structure will be created:
```
├── README.md 
├── main.py 
├── requirements.txt
├── Makefile
├── .gitignore
├── venv/
├── src/
│   ├── module1/
│   │   ├── __init__.py
│   │   └── file1.py
│   ├── settings.py
│   └── path.py
├── tests/
│   └── test_module1.py
├── data/
│   ├── index.html
│   ├── conf.py
│   ├── conf.json
│   └── note.txt
└── debug/
    └── app.log
```

## Installation
Ensure you have Python 3 installed on your system. Then, follow these steps:

1. Clone this repository:
    ```
    git clone https://github.com/samuel-lab/Python-Code-prep.git
    ```
2. Navigate to the project directory:
    ```
    cd python-code-prep
    ```
3. Run:
      For Windows:
    Run ```start.bat```

      For Mac OS and Linux:
    Run ```start.sh```

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvement.

## License
This project is licensed under the [MIT License](LICENSE).

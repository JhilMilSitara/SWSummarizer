import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name= "SessionWise Summarizer"

list_of_files =[
    ".github/workflows/.gitkeep", #for CI/CD deployment whenever you commit the code, this file will take the code  for deployment
    f"src/{project_name}/__init__.py", # this is important as it will consider only the folder having init.py file as the local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating emptyfile : {filepath}")


    else:
        logging.info(f"{filename} already exists")        
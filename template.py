import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]:%(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    #now the filepath has both the things that is file path and filename 
    filedir, filename = os.path.split(filepath)  

    if filedir !="":
        os.makedirs(filedir,exist_ok =True) #checks if the directory is already created or not 
        logging.info(f"Creating Directory ; {filedir} for the file:{filename}")


    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
           #checking if the file exists or not , checking the size of the file 
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file :{filepath}")

    else:
        logging.nfo(f"{filename} already exists")



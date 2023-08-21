import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s - %(message)s]')

name="DIABETES_CLASSIFIER"


list_files=[
    "github/workflows/.gitkeep".format(name),
    "src/{}/__init__.py".format(name),
    "src/{}/components/__init__.py".format(name),
    "src/{}/utils/__init__.py".format(name),
    "src/{}/utils/common.py".format(name),
    "src/{}/config/__init__.py".format(name),
    "src/{}/config/configuration.py".format(name),
    "src/{}/entity/__init__.py".format(name),
    "src/{}/constants/__init__.py".format(name),
    "src/{}/Pipeline/__init__.py".format(name),
    "config/config.yaml",
    "params.yaml",
    "request.yaml",
    "setup.py",
    "research/trails.ipynd",
    "templates/index.html",
    

]

for filename in list_files:
    filepath=Path(filename)
    
    fildir,file=os.path.split(filepath)

    if fildir!="":
        os.makedirs(fildir,exist_ok=True)

        logging.info("basic directory created")

    if (not os.path.exists(filepath)):
        
        with open(filepath,"w") as f:

            logging.info("files are created")
         

            pass

    else:
        logging.info("Already files are creted")

import os
from pathlib import Path
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logs_dir='logs'
logs_path=os.path.join(logs_dir,'current_logs.log')

os.makedirs(logs_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    

    handlers=[
        logging.FileHandler(logs_path),
        logging.StreamHandler(sys.stdout)]
     
    
)


logger=logging.getLogger('DIABETES_CLASSIFIER')
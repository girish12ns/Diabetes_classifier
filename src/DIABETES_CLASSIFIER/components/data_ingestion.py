from src.DIABETES_CLASSIFIER.utils.common import read_yaml,create_directories
from src.DIABETES_CLASSIFIER.constants import config_file_path,param_file_path
from src.DIABETES_CLASSIFIER import logger

import pandas as pd
from sklearn.model_selection import train_test_split


class Data_ingestion:
    def __init__(self,config):
        self.config=config

    
    def get_the_data(self):

        df=pd.read_csv(self.config.source_dir)

        train_set,test_set=train_test_split(df,random_state=42,test_size=0.2)

        train_set.to_csv(self.config.train_dir,index=False,header=True)

        test_set.to_csv(self.config.test_dir,index=False,header=True)

        return(
            self.config.train_dir,
            self.config.test_dir
        )
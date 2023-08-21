from src.DIABETES_CLASSIFIER.utils.common import read_yaml,create_directories
from src.DIABETES_CLASSIFIER.constants import config_file_path,param_file_path
from src.DIABETES_CLASSIFIER import logger
from src.DIABETES_CLASSIFIER.entity.config_entity import DataingestionConfig,Data_TransformationConfig,Model_trainerConfig



class Configuratoration:
    def __init__(self,config=config_file_path,params=param_file_path):
        self.config=read_yaml(config)
        self.params=read_yaml(params)

        create_directories([self.config.artifacts_root])
        
        
       

    def get_data_ingestion_config(self)->DataingestionConfig:
        self.config=self.config.data_ingestion

        create_directories([self.config.root_dir])
       
        config_data_inegstion=DataingestionConfig(
                            root_dir=self.config.root_dir,
                            source_dir=self.config.source_dir,
                            train_dir=self.config.train_dir,
                            test_dir=self.config.test_dir,)

        return config_data_inegstion
    
    
    def get_data_transformation(self) ->Data_TransformationConfig:
        config=self.config.data_transformation
        ingestion=self.config.data_ingestion

        create_directories([config.root_dir])

        transformation=Data_TransformationConfig(
            root_dir=config.root_dir,
            preprocessor_dir=config.preprocessor_dir)

        return (transformation, ingestion)
   
    def get_model_trainer(self)->Model_trainerConfig:
        
        data=self.config.data_ingestion
        trainer=self.config.data_trainer
        transformation=self.config.data_transformation


        create_directories([trainer.root_dir])

        trainer_model=Model_trainerConfig(
            root_dir=trainer.root_dir,
            model_dir=trainer.model_dir
        )



        return (data,transformation,trainer_model)
    






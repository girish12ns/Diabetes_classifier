from src.DIABETES_CLASSIFIER.config.configuration import Configuratoration
from src.DIABETES_CLASSIFIER.components.data_ingestion import Data_ingestion



class Data_ingestionPipeline:
    def __init__(self):
        pass
   
    def main(self):
         configuration=Configuratoration()
         config=configuration.get_data_ingestion_config()

         data=Data_ingestion(config)
         train_set,test_set=data.get_the_data()

try:
    data=Data_ingestionPipeline()
    data.main()

except Exception as e:
    raise e



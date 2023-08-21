from src.DIABETES_CLASSIFIER.config.configuration import Configuratoration
from src.DIABETES_CLASSIFIER.components.data_transformation import Data_Transformation





class Data_transformationPipe:
    def __init__(self):
        pass
   
    def main(self):
        try:
            data=Configuratoration()

            config,ingestion=data.get_data_transformation()

            transformation=Data_Transformation(config,ingestion)

            x_train,x_test,y_test,y_train=transformation.data_tranformation_initiated()

        except Exception as e:
            raise e
         

try:
    data=Data_transformationPipe()
    data.main()

except Exception as e:
    raise e
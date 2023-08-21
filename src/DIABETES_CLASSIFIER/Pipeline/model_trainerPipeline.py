
from src.DIABETES_CLASSIFIER.config.configuration import Configuratoration
from src.DIABETES_CLASSIFIER.components.data_transformation import Data_Transformation
from src.DIABETES_CLASSIFIER.components.model_trainer import Model_trainer

class Model_trainerPipeline:
    def __init__(self):
        pass


    def main(self):
        config=Configuratoration()

        data,transformation,trainer_model=config.get_model_trainer()

        transformation=Data_Transformation(config=transformation,ingestion=data)

        x_train,x_test,y_train,y_test=transformation.data_tranformation_initiated()

    

        model_trainer=Model_trainer(config=trainer_model,data=data,transformation=transformation)

        model_trainer.get_trained_model(x_train,x_test,y_train,y_test)

try:
    triner=Model_trainerPipeline()
    triner.main()
except Exception as e:
    raise e



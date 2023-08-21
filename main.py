from src.DIABETES_CLASSIFIER.Pipeline.data_ingestion_pipeline import Data_ingestionPipeline
from src.DIABETES_CLASSIFIER.Pipeline.data_transformationpipeline import Data_transformationPipe
from src.DIABETES_CLASSIFIER.Pipeline.model_trainerPipeline import Model_trainerPipeline

try:
    data=Data_ingestionPipeline()
    data.main()

except Exception as e:
    raise e


try:
    data=Data_transformationPipe()
    data.main()

except Exception as e:
    raise e


try:
    triner=Model_trainerPipeline()
    triner.main()
except Exception as e:
    raise e

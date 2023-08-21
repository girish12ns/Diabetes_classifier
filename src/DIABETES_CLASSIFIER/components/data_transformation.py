from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
import pandas as pd
from src.DIABETES_CLASSIFIER import logger

from src.DIABETES_CLASSIFIER.utils.common import save_model


class Data_Transformation:
    def __init__(self,config,ingestion):
        self.config=config
        self.ingestion=ingestion
       

    def get_preprocessor_object(self):

        numerical_features=['age','hypertension','heart_disease','bmi','HbA1c_level','blood_glucose_level',]

        cat_features=['gender','smoking_history']

        logger.info("creation of preprocessor_obj")


        #building pipline
        num_pip=Pipeline(steps=[
            ('scaler',StandardScaler()),
            ('impute',SimpleImputer(strategy='mean'))
                ])

        cat_pip=Pipeline(steps=[
                ('coder',OneHotEncoder()),
                ('impuet',SimpleImputer(strategy='most_frequent'))
                ])
        
        preprocessor=ColumnTransformer([
            ('num_pip',num_pip,numerical_features),
            ('cat_pip',cat_pip,cat_features)
           ])


        return preprocessor
    
    def data_tranformation_initiated(self):

        train_df=pd.read_csv(self.ingestion.train_dir)

        test_df=pd.read_csv(self.ingestion.test_dir)

 
        x_train,x_test=(train_df.iloc[:,:-1],test_df.iloc[:,:-1])
        y_train,y_test=(train_df.iloc[:,-1],test_df.iloc[:,-1])


        preprocessor_obj=self.get_preprocessor_object()

        x_train=preprocessor_obj.fit_transform(x_train)

        x_test=preprocessor_obj.transform(x_test)

        save_model(obj=preprocessor_obj,file_path=self.config.preprocessor_dir)


        return (x_train,x_test,y_train,y_test)

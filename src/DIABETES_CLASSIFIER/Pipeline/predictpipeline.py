import os
from src.DIABETES_CLASSIFIER.utils.common import load_model
from pathlib import Path
import pandas as pd



class PredictionPipe:
    def __init__(self):
        pass


    def get_model_data(self,features):

        model=load_model(Path('artifacts\model_trainer\model_trainer.pkl'))

        preprocessor=load_model(Path('artifacts\data_transformation\preprocessor.pkl'))

        data=preprocessor.transform(features)

        predict_data=model.predict(data)

        return predict_data
    
class predict_data:
    def __init__(self,gender:str,age:int,hypertension:int,heart_disease:int,smoking_history:str,bmi:float,HbA1c_level:float,blood_glucose_level:float):
        self.gender=gender
        self.age=age
        self.hypertension=hypertension
        self.heart_disease=heart_disease
        self.smoking_history=smoking_history
        self.bmi=bmi
        self.HbA1c_level=HbA1c_level
        self.blood_glucose_leve=blood_glucose_level


    def get_the_data_frame(self):

        custom_data={
            'gender':[self.gender],
            'age':[self.age],
            'hypertension':[self.hypertension],
            'heart_disease':[self.heart_disease],
            'smoking_history':[self.smoking_history],
            'bmi':[self.bmi],
            'HbA1c_level':[self.HbA1c_level],
            'blood_glucose_level':[self.blood_glucose_leve]}
        
        df=pd.DataFrame(custom_data)

        return df
    

        
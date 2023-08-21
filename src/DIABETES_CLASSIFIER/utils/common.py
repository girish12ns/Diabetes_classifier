import os
from box.exceptions import BoxValueError
import yaml
from src.DIABETES_CLASSIFIER import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import dill

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from catboost import CatBoostClassifier
from xgboost import XGBRFClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,recall_score
from sklearn.neighbors import KNeighborsClassifier
from imblearn.pipeline import Pipeline as imbPipeline
from sklearn.model_selection import GridSearchCV,KFold












@ensure_annotations
def read_yaml(file_path) ->ConfigBox:
    try:
        with open(file_path,'r') as f:
            content=yaml.safe_load(f)
            logger.info("safe loaded {}".format(file_path))
            return ConfigBox(content)
    except BoxValueError as e:
       raise e
    
@ensure_annotations
def create_directories(files_path:list,verbose=True):
    try:
        for file in files_path:
            os.makedirs(file,exist_ok=True)
        if verbose:
                logger.info("The directory created")
    except BoxValueError as e:
        raise e

@ensure_annotations
def save_model(file_path,obj):
    try:
        with open(file_path,'wb') as f:
            dill.dump(obj,f)
            pass
    except BoxValueError as e:
        raise e
try:
    @ensure_annotations
    def model_evalution(true,predict):
        score=accuracy_score(true,predict)
        report=classification_report(true,predict)
        matrix=confusion_matrix(true,predict)
        r_score=recall_score(true,predict)
        return score,report,matrix,r_score
except Exception as e:
    raise e

try:
    def model_prediction(models,x_train,x_test,y_train,y_test):

        r_score_list=[]
        model_list=[]
        score_list=[]

        for i in range(len(list(models))):
            model=list(models.values())[i]
    
            model.fit(x_train,y_train)
    
            predict=model.predict(x_test)
    
            score,report,matrix,r_score=model_evalution(y_test,predict)

            r_score_list.append(r_score)
            model_list.append(list(models.keys())[i])
            score_list.append(score)
            return (model_list,r_score_list,score_list)
except Exception as e:
    raise e







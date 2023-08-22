from src.DIABETES_CLASSIFIER.components.data_transformation import Data_Transformation
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from catboost import CatBoostClassifier
from xgboost import XGBRFClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,recall_score
from sklearn.neighbors import KNeighborsClassifier
from src.DIABETES_CLASSIFIER.utils.common import  model_predictions,save_model


class Model_trainer:
    def __init__(self,config,data,transformation):
        self.config=config
        self.data=data
        self.transformation=transformation
 

    def get_trained_model(self,x_train,x_test,y_train,y_test):
        models={
            'logistic_model':LogisticRegression(),
            'naive_bayes_model':GaussianNB(),
            'svc':SVC(),
            'Decision_tree':DecisionTreeClassifier(),
            'Kn_neighbours':KNeighborsClassifier(),
            'Random_forest':RandomForestClassifier(),
            'Gradient_boosting':GradientBoostingClassifier(),
            'Cat_boosting':CatBoostClassifier(),
            'Xg_boosting':XGBRFClassifier()}
        

        
        model_list,r_score_list,score_list=model_predictions(models=models,x_train=x_train,x_test=x_test,y_train=y_train,y_test=y_test)
        
        model_report={}

        for x,y in zip(model_list,r_score_list):
            model_report[x]=y

        high_values_models=sorted(model_report.items(),key=lambda x:x[1],reverse=True)

        print(high_values_models)

        best_model=models[high_values_models[0][0]]


        save_model(obj=best_model,file_path=self.config.model_dir)
from flask import Flask,render_template,request,url_for
from src.DIABETES_CLASSIFIER.Pipeline.predictpipeline import PredictionPipe,predict_data
from src.DIABETES_CLASSIFIER import logger



app=Flask(__name__)

@app.route('/')
def welcome():
     return render_template('index.html')




@app.route('/predictdata', methods=['GET','POST'])
def predict():
    if request.method=='POST':
        custom_data=predict_data(
            gender=request.form['gender'],
            age=int(request.form['age']),
            hypertension=int(request.form['hypertension']),
            heart_disease=int(request.form['heart_disease']),
            smoking_history=request.form['smoking_history'],
            bmi=float(request.form['bmi']),
            HbA1c_level=float(request.form['HbA1c_level']),
            blood_glucose_level=float(request.form['blood_glucose_level'])

        )
        logger.info("The data has been captures")

        
        pred_df=custom_data.get_the_data_frame()
        print(pred_df)

        data=PredictionPipe()
        result=data.get_model_data(pred_df)
        return render_template('index.html',results=result[0])
      



if __name__=='__main__':
      app.run(host='0.0.0.0',port=8080)
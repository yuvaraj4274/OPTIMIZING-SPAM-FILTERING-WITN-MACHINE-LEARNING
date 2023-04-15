from flask_ngrok import run_with_ngrok
from flask import Flask, render_template
app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')
def text():
  return f"Running Flask on Google Colab"

app.run()
from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd
model=pickle.load(open ("/content/sample_data/model1.pkl",'rb'))

app = Flask (__name__)

@app.route("/")
def home():

  return render_template('/content/Flask/home.html')
@app.route("/content/Flask/predict.html")
def pred():
  return render_template('/content/Flask/predict.html')
@app.route("/pred", methods=['POST', 'GET'])
def predict():
  x = [[int(x) for x in request.form.values()]]
  print(x)
  x = np.array(x)
  print(x.shape)
  print (x)
  pred = model.predict(x)
  print (pred[0])
  return render_template('/content/Flask/submit.html', prediction_text=pred[0])
if __name__ == "__main__":
  !ngrok authtoken "2OBqSJ6TTJQEjqPWIceq38LQj7W_2BmBaC16VDx6dJZG3ERM1" #Without "" marks 
from flask import Flask, render_template
app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')
def hello():
    return render_template('/content/sample_data/index.html', utc_dt=datetime.datetime.utcnow())
app.run()

from flask import Flask,render_template,request,session,redirect,url_for
import numpy 
import pandas
import pickle
import winsound

app=Flask(__name__)
app.secret_key="abhi4040"
model=pickle.load(open('model.pkl','rb'))
vectorizer=pickle.load(open('vectorizer.pkl','rb'))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Prediction",methods=["GET","POST"])
def predict():
    result=""
    try:
        if request.method=="POST":
            message=request.form['mail']
            message=str(message)
            convert=vectorizer.transform([message])
            pre=model.predict(convert)[0]
            if pre==0:
                result="Message is ham"
            else:
                result="Message is spam"
    except Exception as e:
        if e:
            session['er']="Error: "+str(e)
            if session['er']:
                return redirect(url_for("error_handling"))
    return render_template("prediction.html",result=result)

@app.route("/Error")
def error_handling():
    error=session['er']
    return render_template("error.html",Error=error)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=10000)

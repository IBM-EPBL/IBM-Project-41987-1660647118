from flask import render_template,Flask,request
import numpy as np
import pickle 
from sklearn.preprocessing import scale
app= Flask(__name__, template_folder='templates')

rf = pickle.load(open("rdf.pkl",'rb'))


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/')
@app.route('/predict')
def predict():
    return render_template("predict.html")

   
@app.route('/')
@app.route('/submit')
def Submit():
    return render_template("submit.html")


@app.route('/submit',methods = ["GET", "POST"])
def index():
    if request.method=="POST":
        Gender=request.form['Gender']
        Married_Status=request.form['Married_Status']
        Dependents=request.form['Dependents']
        Education=request.form['Education']
        Self_Employed=request.form['Self_Employed']
        Credit_History=request.form['Credit_History']
        Property_Area=request.form['Property_Area']
        Applicant_Income=float(request.form['Applicant_Income'])
        Co_Applicant_Income=float(request.form['Co_Applicant_Income'])
        Loan_Amount=float(request.form['Loan_Amount'])
        Loan_Amount_Term=float(request.form['Loan_Amount_Term'])



        if Gender == 'Male':
            Gender = 1
        else:
            Gender = 0

        if Married_Status == 'Yes':
            Married_Status = 1
        else:
            Married_Status = 0

        if Education == 'Graduate':
            Education = 0
        else:
            Education = 1

        if Self_Employed == 'Yes':
            Self_Employed = 1
        else:
            Self_Employed = 0

        if int(Dependents) >= 3:
            Dependents = 3
        if Credit_History == '1':
            Credit_History = 1
        else:
            Credit_History = 0     
        if Property_Area == 'Urban':
            Property_Area = 2
        elif Property_Area == 'Rural':
            Property_Area = 0
        else:
            Property_Area = 1        
            
        names = [Gender,Married_Status,int(Dependents),Education,Self_Employed,Applicant_Income,Co_Applicant_Income,Loan_Amount,Loan_Amount_Term,Credit_History,Property_Area]
        print(names)
        
        features = [np.array(names)]
        
        prediction = rf.predict(features)

        print(prediction)

        if prediction == 1:
            return render_template('submit.html', result="Congratulations! You are eligible for loan")
        else:
            return render_template('submit.html', result="Sorry! You are not eligible for loan")
    
    else: return render_template("predict.html")

    

if __name__ == "__main__":
    app.run(debug=True, port=5000)
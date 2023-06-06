
# from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import MedicalInsurance
import config
import templates


app = Flask(__name__) # instance
# app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")   #"/" >> home page
def hello_flask():
    print("Welcome to Medical insurance Charges Prediction")
    return render_template("pro_index.html")

@app.route("/predict_charges", methods=["POST", "GET"]) #decorator
def get_insurance_charges():
    if request.method == "GET":
        print("We are using GET Method")    
        # data = request.form
        # print("Data ::",data)

        # age = eval(data["age"])
        # sex = data["sex"]
        # bmi = eval(data["bmi"])
        # children = int(data["children"])
        # smoker = data["smoker"]
        # region = data["region"]

        age = int(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")
        
        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()
        return render_template("pro_index.html", prediction = charges)
        # return jsonify({"result":f"predicted Charges for Medical Insurance is {charges}/- Rs. Only"})  

    else:
        print("We are using POST Method")

        age = int(request.form.get("age"))
        sex = request.form.get("sex")  
        bmi = float(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")

        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()
        return render_template("pro_index.html", prediction = charges)
        # return jsonify({"result":f"predicted Charges for Medical Insurance is {charges}/- Rs. Only"})  

      

if __name__ =="__main__":
    app.run(host = "0.0.0.0", port=3008,debug=True)


    




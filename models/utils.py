import pickle
import json
import pandas as pd
import numpy as np
import config

class MedicalInsurance(): 
    def __init__(self, age, sex, bmi, children, smoker, region):
        self.age = age 
        self.sex = sex 
        self.bmi = bmi 
        self.children = children 
        self.smoker = smoker
        self.region = "region_" + region

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
        # with open("project_model.pkl", "rb") as f:

            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
        # with open("project_data.json") as f:

            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_model() # We have to call method >> load_model >> so that we can use their instance variables
        region_index = self.json_data["columns"].index(self.region)

        array = np.zeros(len(self.json_data["columns"]))
        array[0] = self.age
        array[1] = self.json_data["sex"][self.sex] # label encoding
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.json_data['smoker'][self.smoker]
        array[region_index] = 1 #onehot encoding

        print("Test Array -->\n",array)
        predicted_premium = self.model.predict([array])[0]

        return round(predicted_premium,2)



if __name__ == "__main__":
    age = 67
    sex = "male"
    bmi = 27.9
    children = 3
    smoker = "yes"
    region = "southeast"

    obj = MedicalInsurance(age, sex, bmi, children, smoker, region)
    charges = obj.get_predicted_price()
    print()
    print(f"predicted Charges for Medical Insurance is Rs.{round(charges,2)}/- only")  
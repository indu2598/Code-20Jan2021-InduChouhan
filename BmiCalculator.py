import json
from os import path
class Bmi:
    """
    Bmi class used to represent a BMI Calculator

    Attributes
    ----------
    jsonData : dict
         it stores the json data what we will read from json file

    Methods
    -------
    readJsonFile(filename)
        it take one attritube for filename and reads the json data from the file and store them at jsonData.

    returnData(filename)
        it take one attribute filename and ruturn the jsonDump of jsonData

    CategoryAndHealth(mass)
        it return the dictionary with three keys ['BMI (Body Mass Index)','BMI Category','Health risk'] bases on the mass

    calculateBMIofPerson(filename)
        it calculate the BMI for each entry in jsonData and update the dict with three new colums

    countOverWeight(filename)
        it return the count of person with overweight
    """

    def __init__(self):
        self.jsonData = {}

    def readJsonFile(self,filename):
        self.jsonData = json.load(open(filename, ))

    def returnData(self,filename):
        self.jsonData = json.load(open(filename, ))
        return self.jsonData

    def CategoryAndHealth(self,mass):
        mch = {'BMI (Body Mass Index)' : mass}
        if mass >=0 and mass <= 18.4:
            mch['BMI Category']= "Underweight"
            mch['Health risk'] = "Malnutrition risk"
        elif mass>=18.5 and mass<=24.9:
            mch['BMI Category'] = "Normal weight"
            mch['Health risk'] = "Low risk"
        elif mass>=25 and mass<=29.9:
            mch['BMI Category'] = "Overweight"
            mch['Health risk'] = "Enhanced risk"
        elif mass>=30 and mass<=34.9:
            mch['BMI Category'] = "Moderately obese"
            mch['Health risk'] = "Medium risk"
        elif mass>=35 and mass<=39.9:
            mch['BMI Category'] = "Severely obese"
            mch['Health risk'] = "High risk"
        elif mass>=40:
            mch['BMI Category'] = "Very severely obese"
            mch['Health risk'] = "Very high risk"
        else:
            pass
        return mch

    def calculateBMIofPerson(self,filename):
        filename = filename.split(".")[0]+"output.json"
        for dt in self.jsonData:
            mass = round(dt["WeightKg"]/(dt['HeightCm']/100.0),2)
            mch = self.CategoryAndHealth(mass)
            dt.update(mch)
        a_file = open(filename, "w")
        json.dump(self.jsonData, a_file)
        return self.jsonData

    def countOverWeight(self):
        count = len(list(filter(lambda x : x['BMI Category']=="Overweight",self.jsonData)))
        return count

from BmiCalculator import Bmi
import pytest


@pytest.fixture()
def readingJsonFile():
    """
    This is fixture which will create new Bmi object for each test
    """
    mybmi = Bmi()
    mybmi.readJsonFile('data.json')
    data = mybmi.returnData('data.json')
    return mybmi


def test_ReadJsonFile():
    """
    First Test for reading the data from Json File

    """
    mybmi = Bmi()
    mybmi.readJsonFile('data.json')
    data = mybmi.returnData
    if data:
        assert True
    else:
        assert False

def test_CalculateBMIforEachEntry(readingJsonFile):

    """
    Second test for Calculating BMI for each entry along with BMI Category and Health risk
    """
    data = readingJsonFile.calculateBMIofPerson('data.json')
    if all(map(lambda x:'BMI (Body Mass Index)' in x.keys(),data)):
        assert True
    else:
        assert False

def test_CountOverWeight(readingJsonFile):
    """
    Third test for count Overweight person
    """
    data = readingJsonFile.returnData('dataoutput.json')
    counttest = len(list(filter(lambda x: x['BMI Category'] == "Overweight", data)))
    countcode = readingJsonFile.countOverWeight()
    if counttest==countcode:
        assert True
    else:
        assert False

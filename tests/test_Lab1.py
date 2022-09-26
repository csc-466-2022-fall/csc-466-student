import sys
import os
sys.path.append(".")

import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib 
answers = joblib.load(str(DIR)+"/answers_Lab1.joblib")

# Import the student solutions
import Lab1_helper as helper

import numpy as np
np.random.seed(1)
c = np.random.rand(6,4)

import pandas as pd

credit = pd.read_csv(f"{DIR}/../data/credit.csv",index_col=0)
    
def test_exercise_1():
    X = credit.drop(['Gender','LoanAmountApproved'],axis=1)
    y = credit['LoanAmountApproved']
    model = helper.exercise_1(X,y)

    assert np.all(answers['exercise_1'] == model.coef_)
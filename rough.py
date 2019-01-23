#!/usr/bin/python
import pandas as pd
import numpy as np
# #import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.feature_selection import RFE
# # from sklearn.svm import SVR
# train = datasets.load_iris()

#test_features = df[['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']]
# X, y = make_friedman1(n_samples=50, n_features=10, random_state=0)

# y = train['Species']
# print (y)
# # y[0]=1
# # i=1
# # while (i<y.length):
# #     if y[i]!=y[i-1]:
# #         y[i]=y[i-1]+1
# #     else:
# #         y[i]=y[i-1]
# #     i=i+1

# X = train
# [['Id','SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
# print (X)
# from sklearn.svm import LinearSVC
# from sklearn.svm import SVR
# clf = SVR(kernel="linear")
# clf3 = LinearSVC()
# selector = RFE(clf, 3, step=1)
# selector.fit(train.data, train.target)
# print (selector.score(train.data, train.target))
# print (selector.get_params(True))
# print (selector.get_support(False))
# # # print(df)
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import GridSearchCV
train = pd.read_csv("train.csv")
X = train[['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']]
y = train.Loan_Status
# print (y)
# print (X)
select = SelectKBest(chi2, k=5)
X = select.fit_transform(X, y)
from sklearn.ensemble import RandomForestClassifier  
classifier = RandomForestClassifier(n_estimators=300, random_state=0)
grid_param = {  
    'n_estimators': [100, 300, 500, 800, 1000],
    'criterion': ['gini', 'entropy'],
    'bootstrap': [True, False]
}
gd_sr = GridSearchCV(estimator=classifier,  
                     param_grid=grid_param,
                     scoring='accuracy',
                     cv=5,
                     n_jobs=-1)
gd_sr.fit(X, y)  

best_parameters = gd_sr.best_params_  
print (best_parameters)
print (gd_sr.best_score_)
# print (X_new.shape)
#-----------------------------------------------------------------------
# Imports 
#-----------------------------------------------------------------------
import pandas as pd 
import numpy as np 

from sklearn.neural_network import MLPClassifier 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#-----------------------------------------------------------------------
# Load the dataset 
#-----------------------------------------------------------------------
def Load_data(X):

    print("*"*60)
    print("Load the dataset")
    print(end="\n")


    print("Complete data is : ")
    df=pd.DataFrame(X)

    print(df)
    return df 

#-----------------------------------------------------------------------
# Clean the Dataset 
#-----------------------------------------------------------------------
def Clean_Data(df):
    print("*"*60)
    print("Clean the Dataset")
    print(end="\n")

    print("Total missing values is : ",pd.isnull(df))
    print("First 5 records is : ")
    print(df.head())
    print("*"*60)
    return df 


#-----------------------------------------------------------------------
# Applying standard scalar
#-----------------------------------------------------------------------
def Scalar(X_train):


    print("*"*60)
    print("Applying standard scalar")
    print(end="\n")
    
    scalar=StandardScaler()
    X_train_scaled =scalar.fit_transform(X_train) 

    print("*"*60)
    return X_train_scaled

#-----------------------------------------------------------------------
# FNN model 
#-----------------------------------------------------------------------

def FNN(X_train_scaled,Y_train):
    print("*"*60)
    model = MLPClassifier(
        hidden_layer_sizes=(12,8),
        max_iter=1000,
        random_state=42,
        solver="adam",
        activation="relu"

    )

    model.fit(X_train_scaled,Y_train)


    print("FNN model created successfully ")
    print(end="\n")

    print("*"*60)
    return model 
#-----------------------------------------------------------------------
# Testing the model 
#-----------------------------------------------------------------------
def Test_model(model):
    Y_test=[1]
    X_test=[[55000,720,400000,10000,1]]
    Y_pred=model.predict(X_test)
    return Y_pred,Y_test

#-----------------------------------------------------------------------
# Evaluate the model 
#-----------------------------------------------------------------------

def Evaluate(Y_test,Y_pred):


    print("*"*60)
    print("Evaluating the model")
    print(end="\n")

    print("Accuracy is  : ")
    acc=accuracy_score(Y_test,Y_pred)
    print(acc)

    print("Output Prediction : ")
    if(acc==1):
        print("Employment Status :  Stable")
    else :
        print("Employment Status : Not Stable")


    

    print("*"*60)

#-----------------------------------------------------------------------
# Main Function 
#-----------------------------------------------------------------------

def main():

    X=[

        [25000, 600, 200000, 10000, 0],
        [40000, 700, 300000, 8000, 1],
        [60000, 750, 500000, 12000, 1],
        [20000, 550, 150000, 15000, 0],
        [80000, 800, 700000, 10000, 1],
        [35000, 650, 250000, 9000, 1],
        [18000, 500, 100000, 12000, 0],
        [90000, 850, 800000, 15000, 1],
        [30000, 580, 200000, 14000, 0],
        [70000, 780, 600000, 10000, 1]
    ]
    
    Y_train=[
        0,1,1,0,1,
        1,0,1,0,1
    ]

    df=Load_data(X)
    df=Clean_Data(df)
    X_train_scaled=Scalar(X)
    model=FNN(X_train_scaled,Y_train)
    Y_pred,Y_test=Test_model(model)
    Evaluate(Y_test,Y_pred)

if __name__=="__main__":
    main()

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
    X_test=[[46,1450,5,6,9]]
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
        print("Customer may leave ")
    else :
        print("Customer will stay ")

    

    print("*"*60)

#-----------------------------------------------------------------------
# Main Function 
#-----------------------------------------------------------------------

def main():

    X=[
        [25,500,12,1,2],
        [30,700,24,0,1],
        [45,1200,6,5,8],
        [50,1500,5,6,10],
        [28,600,18,1,1],
        [35,800,30,0,0],
        [48,1400,4,7,9],
        [52,1600,3,8,12],
        [27,550,20,0,11],
        [42,1300,8,4,7]
    ]
    
    Y_train=[
        0,0,1,1,0,
        0,1,1,0,1
    ]
    df=Load_data(X)
    df=Clean_Data(df)
    X_train_scaled=Scalar(X)
    model=FNN(X_train_scaled,Y_train)
    Y_pred,Y_test=Test_model(model)
    Evaluate(Y_test,Y_pred)

if __name__=="__main__":
    main()

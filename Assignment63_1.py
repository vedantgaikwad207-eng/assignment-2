#-------------------------------------------------------------------------------------------
# Imports 
#-------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

#-------------------------------------------------------------------------------------------
#   Function Name : Load_Data()
#   Description   : Load the csv and also evaluate the csv    
#   Input         : Datapath 
#   output        : Dataset 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------

def Load_Data(Datapath):
    df=pd.read_csv(Datapath)
    print("Shape of Dataset is : ", df.shape)
    print("Columns of dataset is : ", df.columns)
    print("First Five records are : ")
    print(df.head())

    return df

#-------------------------------------------------------------------------------------------
#   Function Name : mising_values()
#   Description   : Check for mising values and identify and modify the categorical features   
#   Input         : dataset (df) 
#   output        : modified dataset (df) 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------
def mising_values(df):
    print("Total mising values are : ", df.isnull().sum())

    
    for column in df.columns : 
        unique=df[column].nunique()
        if(unique==2):
            print(f"Categorical classification : {column}")
        if(unique>2):
            print(f"Numerical classification : {column}")

    #--------------------
    # Own = 1 , Rent = 0 , Mortgage = 2
    #--------------------
    df["PreviousDefault"]=df["PreviousDefault"].map({"Yes":1,"No":0})
    df["HomeOwnership"]=df["HomeOwnership"].map({"Own":1,"Rent":0,"Mortgage":2})

    print("Modified dataset is : ")
    print(df.head())
    

    return df

#-------------------------------------------------------------------------------------------
#   Function Name : Sep_features()
#   Description   : Seperate the independent and dependent features    
#   Input         : Dataset (df) 
#   output        : Independent (X) and dependent (Y) variables 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------

def Sep_features(df):
    X=df.drop(["Default"],axis=1)
    Y=df["Default"]

    print("First Five records are : ")
    print("Independent variables : ")
    print(X.head())
    print("Dependent variables : ")
    print(Y.head())

    return X,Y


#-------------------------------------------------------------------------------------------
#   Function Name : Split_Data()
#   Description   : Split the dataset into training and testing    
#   Input         : X,Y 
#   output        : X_train,X_test,Y_train,Y_test 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------
def Split_Data(X,Y):
    X_train,X_test,Y_train,Y_test=train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=42

    )
    print("Shape of training dataset is : ", X_train.shape)
    print("Shape of testing dataset is : ", X_test.shape)

    return X_train,X_test,Y_train,Y_test


#-------------------------------------------------------------------------------------------
#   Function Name : Scale_Features()
#   Description   : Feature Scaling    
#   Input         : X_train,X_test 
#   output        : X_train_scaled,X_test_scaled,scalar
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------

def Scale_Features(X_train,X_test):
    scalar=StandardScaler()
    X_train_scaled=scalar.fit_transform(X_train)
    X_test_scaled=scalar.fit_transform(X_test)
    return X_train_scaled,X_test_scaled,scalar

#-------------------------------------------------------------------------------------------
#   Function Name : MLP()
#   Description   : 1.Create the MLP and trained the model 
#                   2.Displaying the no. of iterations required     
#   Input         : X_train_scaled,X_test_scaled,Y_train,Y_test
#   output        : Y_pred,model 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------
def MLP(X_train_scaled,X_test_scaled,Y_train,Y_test):
    model=MLPClassifier(
        hidden_layer_sizes=(12,8),
        solver="adam",
        activation="relu",
        random_state=42,
        max_iter=1000
    )
    model.fit(X_train_scaled,Y_train)
    iterations=model.n_iter_
    print(f"The model trained in {iterations} iterations ")
    Y_pred=model.predict(X_test_scaled)

    return Y_pred,model


#-------------------------------------------------------------------------------------------
#   Function Name : Evaluate()
#   Description   : Evaluate the model   
#   Input         : Y_test,Y_pred 
#   output        : None 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------
def Evaluate(Y_test,Y_pred):
    print("Testing Accuracy is : ")
    print(accuracy_score(Y_test,Y_pred))
    print("Confusion matrix : ")
    print(confusion_matrix(Y_test,Y_pred))
    print("Classification report is : ")
    print(classification_report(Y_test,Y_pred))

#-------------------------------------------------------------------------------------------
#   Function Name : loss_curve()
#   Description   : Plots the loss curve    
#   Input         : model 
#   output        : None 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------
def loss_curve(model):
    plt.plot(model.loss_curve_)
    plt.title("Loss Curve ")
    plt.xlabel("Iterations ")
    plt.ylabel("Loss ")
    plt.show()

#-------------------------------------------------------------------------------------------
#   Function Name : preserve()
#   Description   : preserve the model   
#   Input         : model,scalar 
#   output        : None 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------
def preserve(model,scalar):
    joblib.dump(model,"Loan_Default.pkl")
    joblib.dump(scalar,"scalar.pkl")
#-------------------------------------------------------------------------------------------
#   Function Name : PredictAttrition()
#   Description   : 1.Testing the Data with new inputs
#                   2.Displaying the accuracy     
#   Input         : None 
#   output        : None 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------
def PredictAttrition():
    load_model=joblib.load("Loan_Default.pkl")
    load_scalar=joblib.load("scalar.pkl")

    new_Loan_data = {} # Test the model for prediction 
    df=pd.DataFrame(new_Loan_data)
    df=load_scalar.transform(df)
    new_pred=load_model.predict(df)
    Y_true=[]   # Actual Answer 
    print("Accuracy of new data is : ")
    print(accuracy_score(new_pred,Y_true)*100)



#-------------------------------------------------------------------------------------------
#   Function Name : main()
#   Description   : Call all the function   
#   Input         : None 
#   output        : None 
#   Author        : Vedant Gaikwad
#   Date          : 08/09/26

#-------------------------------------------------------------------------------------------

def main():
    Datapath="Loan_Default.csv"
    df=Load_Data(Datapath)
    df =mising_values(df)
    X,Y=Sep_features(df)
    X_train,X_test,Y_train,Y_test=Split_Data(X,Y)
    X_train_scaled,X_test_scaled,scalar=Scale_Features(X_train,X_test)
    Y_pred,model=MLP(X_train_scaled,X_test_scaled,Y_train,Y_test)
    loss_curve(model)
    preserve(model,scalar)
    PredictAttrition()
    

if __name__=="__main__":
    main()
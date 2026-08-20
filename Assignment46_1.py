import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def main():
    Border="*"*50
    ############################################
    # Load the Data
    ############################################
    print(Border)
    print("Load the Data")
    print(Border)
    Datapath="Advertising.csv"
    df=pd.read_csv(Datapath)
    print(df.head())
    print("Data loaded successfully")

    ############################################
    # Handling mising values 
    ############################################
    print(Border)
    print("Handling mising values")
    print(Border)

    print("Total mising values : ",df.isnull().sum())
    df=df.drop(columns=["Unnamed: 0"])
    print("Dataset after removing unnamed column is : ")
    print(df.head())

    ############################################
    # Spliting of Independent and dependent variables 
    ############################################
    print(Border)
    print("Spliting of Independent and dependent variables")
    print(Border)

    X=df[["TV","radio","newspaper",]]
    Y=df["sales"]
    print("Independent variables :")
    print(X.head())
    print("Dependent variables is :")
    print(Y.head())

    ############################################
    # split the Dataset
    ############################################
    print(Border)
    print("split the Dataset")
    print(Border)
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.3)
    print("Training Dataset :",X_train.head())
    print("Testing Dataset :",X_test.head())
    print("Spliting of Dataset done ")
    ############################################
    # Train and Test the model
    ############################################
    print(Border)
    print("Train and Test the model")
    print(Border)
    model=LinearRegression()
    model=model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test)

    print("Expected answer : ")
    print(list(Y_test))
    print("Predicted answer : ")
    print(Y_pred)

    ############################################
    # Evaluate the model
    ############################################
    print(Border)
    print("Evaluate the model")
    print(Border)
    MSE=mean_squared_error(Y_test,Y_pred)
    RMSE=np.sqrt(MSE)
    R2=r2_score(Y_test,Y_pred)
    print("Mean squared error is :",MSE)
    print("Root Mean squared error is :",RMSE)
    print("R2_score value : ",R2)

    

if __name__=="__main__":
    main()
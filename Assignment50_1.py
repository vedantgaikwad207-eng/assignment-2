import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
def Cancer(Datapath):
    Border="*"*100
##########################################################################################
# Load the Data
##########################################################################################
    print(Border)
    print(Border)

    print("Load the Data")
    print(Border)
    print(Border)

    df=pd.read_csv(Datapath)

    print(df.head())
    print(Border)
##########################################################################################
# Handle the mising values 
##########################################################################################
    print(Border)
    print(Border)
    print("Handle the mising values ")
    print(Border)
    df.replace("?",np.nan,inplace=True)
    print("Total mising values : ",df.isnull().sum())
    num=SimpleImputer(strategy="median")
    df["BareNuclei"]=num.fit_transform(df[["BareNuclei"]])


##########################################################################################
# Exploratory data analysis
##########################################################################################
    print(Border)
    print(Border)
    print("Exploratory data analysis")
    print(Border)

    print("Summary Statistics :")
    print(df.describe())

    print(Border)
    print("Correlation :")
    print(df.corr())

##########################################################################################
# Spliting the dataset into training and testing 
##########################################################################################
    print(Border)
    print(Border)
    print("Spliting the dataset into training and testing ")
    print(Border)

    X=df[["ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses"]]

    print("Independent Variable is :")
    print(X.head())
    print(Border)
    Y=df["CancerType"]
    print("Dependent Variable is : ")
    print(Y.head())
    print(Border)
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.4,random_state=42)
    print("Training Dataset is :")
    print(X_train.shape)
    print("Testing Dataset is :")
    print(X_test.shape)

##########################################################################################
# Model creation 
##########################################################################################
    print(Border)
    print(Border)

    print("Model creation ")
    print(Border)
    model=DecisionTreeClassifier()
    model=model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test)
    print("Expected Answer is : ")
    print(list(Y_test))
    print("Predicted Answer is : ")
    print(Y_pred)

##########################################################################################
# Evaluate the model
##########################################################################################
    print(Border)
    print(Border)
    print("Evaluate the model")
    print(Border)

    print("Accuracy is : ")
    Accuracy=accuracy_score(Y_test,Y_pred)
    print(Accuracy*100)

    print("Confusion matrix is :")
    print(confusion_matrix(Y_test,Y_pred))
    
    print("Classification report is : ")
    print(classification_report(Y_test,Y_pred))


    print("----------------------End of the program---------------------------------- ")
    print("-------------------------Thank You----------------------------------------")    
    print(Border)
    print(Border)










def main():
    Datapath="breast-cancer-wisconsin.csv"
    Cancer(Datapath)

if __name__=="__main__":
    main()
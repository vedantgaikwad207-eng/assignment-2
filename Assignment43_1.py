from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
def CheckAccuracy(X,Y):
    accuracy=accuracy_score(X,Y)
    return accuracy*100


def main():
    Border="*"*50
####################################################
#  Step 1 : Load the file
####################################################
    print(Border)
    Datapath="MarvellousInfosystems_PlayPredictor.csv"
    df=pd.read_csv(Datapath)
    print("First 5 info is :")
    print(df.head())
    print(Border)
#####################################################
#  Encoding the Dataset
#####################################################
    encoder = LabelEncoder()

    for column in df.columns:
        df[column]=encoder.fit_transform(df[column])
    

####################################################
#  Step 2 : Clean the dataset
####################################################

    df.dropna(inplace=True)
    print("Dataset is cleaned ")
    print(Border)





####################################################
#   Step 3 : Spliting the independent and dependent variable
####################################################

    X=df.drop(columns="Play")
    Y=df["Play"]
    print(Border)

    print("Shape of Independent variable :",X.shape)
    print("Shape of Dependent variable : ",Y.shape)
    print(Border)






#####################################################
#   Step 4 : Split the dataset 
#####################################################

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
    print(Border)

    print("Shape of X train",X_train.shape)
    print("Shape of X test",X_test.shape)
    print("Shape of Y train",Y_train.shape)
    print("Shape of Y test",Y_test.shape)
    print(Border)

   
########################################################
#  Step 5 : Hyperparameter tuning
########################################################
    
    
    model=KNeighborsClassifier(n_neighbors=3)
    model=model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test)
    print("Actual answer : ",list(Y_test))
    print("Predicted answer : ",Y_pred)
    accuracy=CheckAccuracy(Y_test,Y_pred)
    print("Accuracy is : ",accuracy)
        



if __name__=="__main__":
    main()
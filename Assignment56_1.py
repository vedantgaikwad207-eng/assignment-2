Border="*"*80

#-----------------------------------------------------------------
# Importing libraries 
#-----------------------------------------------------------------

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier,BaggingClassifier,AdaBoostClassifier,RandomForestClassifier

#-----------------------------------------------------------------
#   Function Name : Data_Load()
#   Description   : Dataset loading  function
#   Input         : Datapath
#   output        : Dataset
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Data_Load(Datapath):
    print(Border)
    df= pd.read_csv(Datapath)
    print("Data loaded successfully",end="\n")
    print("First Five records are : ")
    print(df.head())
    print(Border)
    return df 

#-----------------------------------------------------------------
#   Function Name : Mising_Values()
#   Description   : Checking Mising values in Dataset
#   Input         : Dataset(df)
#   output        : None
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Mising_Values(df):
    print(Border)
    print("Total mising values is : ",df.isnull().sum()) 
    print(Border)

#-----------------------------------------------------------------
#   Function Name : Seperate_data()
#   Description   : Seperating the independent and dependent variable
#   Input         : Dataset(df)
#   output        : Independent variable(X) and dependent varible(Y)
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Seperate_data(df):
    X=df.drop("Fraud",axis=1)
    Y=df["Fraud"]
    print(Border)
    print("Independent Variable X is : ")
    print(X.head())
    print("\n Dependent variables Y is : ")
    print(Y.head())
    print(Border)
    return X,Y


#-----------------------------------------------------------------
#   Function Name : Scaling()
#   Description   : performing feature scaling
#   Input         : Independent variable(X)
#   output        : X
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Scaling(X):
    scalar=StandardScaler()
    X=scalar.fit_transform(X)

    return X

#-----------------------------------------------------------------
#   Function Name : Split_test_train()
#   Description   : Dataset spliting function
#   Input         : X,Y
#   output        : X_train,X_test,Y_train,Y_test
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Split_test_train(X,Y):
    print(Border)
    X_train,X_test,Y_train,Y_test=train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=42
    )
    print("\n Spliting of Dataset into training and testing data done ")
    print(Border)
    return X_train,X_test,Y_train,Y_test


#-----------------------------------------------------------------
#   Function Name : Train_Test()
#   Description   : Training the model
#   Input         : X_train,Y_train,X_test
#   output        : Y_pred1,Y_pred2,Y_pred3,Y_pred4,Y_pred5
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Train_Test(X_train,Y_train,X_test):
    
    
    model1=DecisionTreeClassifier(random_state=42)
    model1.fit(X_train,Y_train)
    Y_pred1=model1.predict(X_test)

    base_model=DecisionTreeClassifier(random_state=42)
    model2=BaggingClassifier(
        estimator=base_model,
        n_estimators=10,
        random_state=42
    )
    model2.fit(X_train,Y_train)
    Y_pred2=model2.predict(X_test)

    model3=RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )
    model3.fit(X_train,Y_train)
    Y_pred3=model3.predict(X_test)


    model4=AdaBoostClassifier(
        n_estimators=100,
        learning_rate=0.1,
        random_state=42
    )
    model4.fit(X_train,Y_train)
    Y_pred4=model4.predict(X_test)

    model1=LogisticRegression(max_iter=1000)
    model2=DecisionTreeClassifier(random_state=42)
    model3=KNeighborsClassifier(n_neighbors=6)
    model5=VotingClassifier(
        [("Logistic",model1),
        ("Decision",model2),
        ("KNN",model3)
        ],
        voting="hard"


    )
    model5=model5.fit(X_train,Y_train)
    Y_pred5=model5.predict(X_test)

        
    print(Border)
    print("Model trained successfully ")
    print(Border)
    return Y_pred1,Y_pred2,Y_pred3,Y_pred4,Y_pred5



#-----------------------------------------------------------------
#   Function Name : Display()
#   Description   : Evaluating the model  
#   Input         : Y_test,Y_pred1,Y_pred2,Y_pred3,Y_pred4,Y_pred5
#   output        : None 
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Display(Y_test,Y_pred1,Y_pred2,Y_pred3,Y_pred4,Y_pred5):
    print(Border)
    print("\n")
    print("\n")

    print("Decision Tree ")
    print("Confusion Matrix for Decision tree is : ")
    print(confusion_matrix(Y_test,Y_pred1))
    print("Classification report is : ")
    print(classification_report(Y_test,Y_pred1))
    print("\n")

    print("Bagging Classifier")
    print("Confusion Matrix  is : ")
    print(confusion_matrix(Y_test,Y_pred2))
    print("Classification report is : ")
    print(classification_report(Y_test,Y_pred2))
    print("\n")

    print("Random forest classifier ")
    print("Confusion Matrix is : ")
    print(confusion_matrix(Y_test,Y_pred3))
    print("Classification report is : ")
    print(classification_report(Y_test,Y_pred3))
    print("\n")

    print("Adaboost Classifier")
    print("Confusion Matrix is : ")
    print(confusion_matrix(Y_test,Y_pred4))
    print("Classification report is : ")
    print(classification_report(Y_test,Y_pred4))
    print("\n")

    print("Voting classifier")
    print("Confusion Matrix is : ")
    print(confusion_matrix(Y_test,Y_pred5))
    print("Classification report is : ")
    print(classification_report(Y_test,Y_pred5))
    print("\n")

    print("\n")
    print(Border)


#-----------------------------------------------------------------
#   Function Name : main()
#   Description   : Call all the function   
#   Input         : None 
#   output        : None 
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------


def main():
    Datapath="Fraudulent_Transaction_Detection.csv"
    df=Data_Load(Datapath)
    Mising_Values(df)
    X,Y= Seperate_data(df)
    X=Scaling(X)
    X_train,X_test,Y_train,Y_test=Split_test_train(X,Y)
    Y_pred1,Y_pred2,Y_pred3,Y_pred4,Y_pred5=Train_Test(X_train,Y_train,X_test)
    
    Display(Y_test,Y_pred1,Y_pred2,Y_pred3,Y_pred4,Y_pred5)


if __name__=="__main__":
    main()


#------------------------------------------------------------------
#                         End of the program 
#------------------------------------------------------------------

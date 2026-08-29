Border="*"*80

#-----------------------------------------------------------------
# Importing libraries 
#-----------------------------------------------------------------

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier

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
    X=df[["Age","Income","CreditScore","ExistingLoan","EmploymentExperience","LoanAmount"]]
    Y=df["LoanApproved"]
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
#   output        : Y_pred1,Y_pred2,Y_pred3
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Train_Test(X_train,Y_train,X_test):
    model1=LogisticRegression(max_iter=1000)
    model1.fit(X_train,Y_train)
    Y_pred1=model1.predict(X_test)

    
    model2=DecisionTreeClassifier(random_state=42)
    model2.fit(X_train,Y_train)
    Y_pred2=model2.predict(X_test)


    model3=KNeighborsClassifier(n_neighbors=6)
    model3.fit(X_train,Y_train)
    Y_pred3=model3.predict(X_test)

    print(Border)
    print("Model trained successfully ")
    print(Border)
    return Y_pred1,Y_pred2,Y_pred3

#-----------------------------------------------------------------
#   Function Name : Accuracy)
#   Description   : Training the model
#   Input         : Y_pred1,Y_pred2,Y_pred3,Y_test
#   output        : Accuracy1*100,Accuracy2*100,Accuracy3*100
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Accuracy(Y_pred1,Y_pred2,Y_pred3,Y_test):
    
    Accuracy1=accuracy_score(Y_test,Y_pred1)
    Accuracy2=accuracy_score(Y_test,Y_pred2)
    Accuracy3=accuracy_score(Y_test,Y_pred3)

    return Accuracy1*100,Accuracy2*100,Accuracy3*100


#-----------------------------------------------------------------
#   Function Name : voting_hard()
#   Description   : Using voting classifier for hard voting 
#   Input         : X_train,X_test,Y_train,Y_test
#   output        : Accuracy of hard voting 
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def voting_hard(X_train,X_test,Y_train,Y_test):
    model1=LogisticRegression(max_iter=1000)
    model2=DecisionTreeClassifier(random_state=42)
    model3=KNeighborsClassifier(n_neighbors=6)
    model=VotingClassifier(
        [("Logistic",model1),
        ("Decision",model2),
        ("KNN",model3)
        ],
        voting="hard"


    )
    model=model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test)
    Accuracy_hard=accuracy_score(Y_test,Y_pred)

    return Accuracy_hard*100

#-----------------------------------------------------------------
#   Function Name : voting_soft()
#   Description   : Using voting classifier for soft voting  
#   Input         : X_train,X_test,Y_train,Y_test
#   output        : Accuracy of soft voting 
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def voting_soft(X_train,X_test,Y_train,Y_test):
    model1=LogisticRegression(max_iter=1000)
    model2=DecisionTreeClassifier(random_state=42)
    model3=KNeighborsClassifier(n_neighbors=6)
    model=VotingClassifier(
        [("Logistic",model1),
        ("Decision",model2),
        ("KNN",model3)
        ],
        voting="soft"


    )
    model=model.fit(X_train,Y_train)
    Y_pred=model.predict(X_test)
    Accuracy_soft=accuracy_score(Y_test,Y_pred)

    return Accuracy_soft*100

#-----------------------------------------------------------------
#   Function Name : Display()
#   Description   : Evaluating the model  
#   Input         : Accuracy1,Accuracy2,Accuracy3,Accuracy_hard,Accuracy_soft
#   output        : None 
#   Author        : Vedant Gaikwad
#   Date          : 28/08/26
#-----------------------------------------------------------------

def Display(Accuracy1,Accuracy2,Accuracy3,Accuracy_hard,Accuracy_soft):
    print(Border)
    print("\n")
    print("\n")

    print("Model                         |            Accuracy")
    print(f"Logistic regression           |                {Accuracy1}")
    print(f"Decision Tree                 |                {Accuracy2}")
    print(f"KNN                           |                {Accuracy3}")
    print(f"Hard voting                   |                {Accuracy_hard}")
    print(f"Soft voting                   |                {Accuracy_soft}")

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
    Datapath="Customer_Loan_Approval.csv"
    df=Data_Load(Datapath)
    Mising_Values(df)
    X,Y= Seperate_data(df)
    X=Scaling(X)
    X_train,X_test,Y_train,Y_test=Split_test_train(X,Y)
    Y_pred1,Y_pred2,Y_pred3=Train_Test(X_train,Y_train,X_test)
    Accuracy1,Accuracy2,Accuracy3=Accuracy(Y_pred1,Y_pred2,Y_pred3,Y_test)
    Accuracy_hard=voting_hard(X_train,X_test,Y_train,Y_test)
    Accuracy_soft=voting_soft(X_train,X_test,Y_train,Y_test)
    Display(Accuracy1,Accuracy2,Accuracy3,Accuracy_hard,Accuracy_soft)


if __name__=="__main__":
    main()


#------------------------------------------------------------------
#                         End of the program 
#------------------------------------------------------------------

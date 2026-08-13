from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.metrics import accuracy_score,ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
def main():
    Datapath="student_performance_ml.csv"

    df = pd.read_csv(Datapath)
    Features_col=["StudyHours",
                  "Attendance",
                  "PreviousScore",
                  "AssignmentsCompleted",
                  "SleepHours"
                  ]
    
    X=df[Features_col]
    Y=df["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=42)

# Model no.1 (random_state=0)
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=0)

    model = DecisionTreeClassifier()
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print("predicted answer :")
    print(Y_pred)
    print("Actual Answer : ")
    print(Y_test)
    accuracy = accuracy_score(Y_test , Y_pred)
    print("Accuracy is : " , accuracy*100)

# Model No. 2 (random_state=10)
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=10)

    model = DecisionTreeClassifier(max_depth=3)
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print("predicted answer :")
    print(Y_pred)
    print("Actual Answer : ")
    print(Y_test)
    accuracy = accuracy_score(Y_test , Y_pred)
    print("Accuracy is : " , accuracy*100)

# Model No.3 (random_state=42)
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=42)


    model = DecisionTreeClassifier(max_depth=None )
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print("predicted answer :")
    print(Y_pred)
    print("Actual Answer : ")
    print(Y_test)

    accuracy = accuracy_score(Y_test , Y_pred)
    print("Accuracy is : " , accuracy*100)   
    
    


if __name__=="__main__":
    main()
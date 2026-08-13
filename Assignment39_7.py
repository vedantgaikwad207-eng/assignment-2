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

    model = DecisionTreeClassifier()
    model.fit(X_train,Y_train)
    label=[["6","85","66","7","7"]]
    Y_pred = model.predict(label)


    print("predicted answer :")
    print(Y_pred)
    print("Actual Answer : ")
    print(Y_test)
    if (Y_pred==1):
        print("Pass")
    else:
        print("failed")



    


if __name__=="__main__":
    main()
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
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

    Y_pred = model.predict(X_test)

    print("predicted answer :")
    print(Y_pred)
    print("Actual Answer : ")
    print(Y_test)





if __name__=="__main__":
    main()
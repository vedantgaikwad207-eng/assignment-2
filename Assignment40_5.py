import pandas as pd
from sklearn.metrics import accuracy_score , ConfusionMatrixDisplay,classification_report 
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():
#    Data loading     #
    Datapath="student_performance_ml.csv"
    df = pd.read_csv(Datapath)

#    Data analysis    # 

    value=df.isnull().sum()
    print("Total null values are : ")
    print(value)

#    Visualization    #

    for sp in df["FinalResult"].unique():
        temp=df[df["FinalResult"]==sp]
        plt.scatter(temp["Attendance"],temp["PreviousScore"],label=sp)

    plt.title("Attendance Vs PreviousScore")
    plt.xlabel("Attendance")
    plt.ylabel("PreviousScore")

    plt.show()

#    Train test split  #

    Features_col=["StudyHours",
                  "Attendance",
                  "PreviousScore",
                  "AssignmentsCompleted",
                  "SleepHours"
                  ]
    
    X=df[Features_col]
    Y=df["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.5,random_state=42)

#    Model training     # 
    model= DecisionTreeClassifier()
    model.fit(X_train , Y_train)



#   Prediction         # 

    Y_pred = model.predict(X_test)
    print("predicted answer :")
    print(Y_pred)
    print("Actual Answer : ")
    print(Y_test)    

#    Accuracy Calculation  #
    total=0
    correct =0
    j=0
    Y_testL=[]
    for i in Y_test:
        Y_testL.append(i)
    for i in Y_pred:
        total=total+1
        if(i==Y_testL[j]):
            correct=correct+1
        j=j+1
    accuracy = (correct/total)*100
    print("Accuracy is : " , accuracy)


if __name__=="__main__":
    main()
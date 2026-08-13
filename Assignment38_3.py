import pandas as pd
def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Average Study Hours : ")

    y= list(df["StudyHours"])
    sum=0
    Total=0
    for i in y :
        sum=sum+i
        Total=Total+1

    Avg = sum/Total

    print(Avg)

    y = list(df["Attendance"])
    sum=0
    Total=0
    for i in y :
        sum=sum+i
        Total=Total+1
    
    Avg = sum/Total
    print("Average Attendence : ")    
    print(Avg)

    y=list(df["PreviousScore"])
    max=0
    min=0
    for i in y :
        if(max<i):
            max=i

    for i in y :
        if(max>i):
            min=i
    

    
    print("Maximum Previous score : ")
              
    print(max)
    print("Minimum Previous score : ")
    print(min)
    



if __name__=="__main__":
    main()


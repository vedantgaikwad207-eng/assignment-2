import pandas as pd
def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print(df["FinalResult"].value_counts())


    
    y=list(df["FinalResult"])
    Total=0
    Pass=0
    Unsuccessful = 0
    for i in y :
        Total=Total+1
        if(i==1):
            Pass=Pass+1
        else :
            Unsuccessful=Unsuccessful+1

    PassPercen=(Pass/Total)*100
    UnPercen=(Unsuccessful/Total)*100

    print("Pass Percentage : ")
    print(PassPercen)
    print("Failed Percentage : ")
    print(UnPercen)

    y=df["FinalResult"].value_counts(normalize=True)
    Minor = y.min()

    if(Minor<=0.10):
        print("Unbalanced ")
    else :
        print("Balanced ")

    







if __name__=="__main__":
    main()


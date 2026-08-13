import pandas as pd
def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Total no. of students are : ")
    print(len(df.index))

    print("No. of students passed : ")
    y=list(df["FinalResult"])
    
    Pass=0
    Unsuccessful = 0
    for i in y :
        if(i==1):
            Pass=Pass+1
        else :
            Unsuccessful=Unsuccessful+1

    print(Pass)
    print("No. of students failed : ")
    print(Unsuccessful)


if __name__=="__main__":
    main()


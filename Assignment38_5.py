import pandas as pd
def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    # Min contain the student who passed by studying for minimum hours from that all students who passed 
    Min = df[df["FinalResult"]==1]["StudyHours"].min()  
    
    Max = df[df["FinalResult"]==0]["StudyHours"].max()

    print("The students that failed after maximum study for ")
    print(Max,"hours")
    print("The students that passed after minimum study for ")
    print(Min,"hours")

    if(Max<Min):
        print("Higher Study Hours Increase the chance of passing")
    else :
        print("Higher Study Hours doesnt Increase the chance of passing")

    Min=df[df["FinalResult"]==1]["Attendance"].min()
    Max=df[df["FinalResult"]==0]["Attendance"].max()

    print("The students that failed after giving maximum attendance for ")
    print(Max)
    print("The students that Passed after giving minimum attendance for ")
    print(Min)

    if(Max<Min):
        print("Higher Attendance improves the final result")
    else :
        print("Higher Attendance doesnt improves the final result")


    

        






if __name__=="__main__":
    main()


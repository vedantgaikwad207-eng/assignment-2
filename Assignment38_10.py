import pandas as pd 
import matplotlib.pyplot as plt
def main():
    Datapath="student_performance_ml.csv"

    df=pd.read_csv(Datapath)

    for sp in df["FinalResult"].unique():
        temp=df[df["FinalResult"]==sp]
        plt.scatter(temp["SleepHours"],temp["FinalResult"],label=sp)

    plt.title("SleepHours Vs FinalResult ")
    plt.xlabel("SleepHours ")
    plt.ylabel("FinalResult")

    plt.show()

if __name__=="__main__":
    main()

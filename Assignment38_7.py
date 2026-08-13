import pandas as pd
import matplotlib.pyplot as plt 
def main():

    Datapath="student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    for sp in df["FinalResult"].unique():
        temp=df[df["FinalResult"]==sp]
        plt.scatter(temp["StudyHours"],temp["PreviousScore"],label=sp)

    plt.title("StudyHours Vs PreviousStore")
    plt.xlabel("Study Hours ")
    plt.ylabel("PreviousScore")
    plt.legend()
    plt.grid()
    plt.show()

if __name__=="__main__":
    main()
    

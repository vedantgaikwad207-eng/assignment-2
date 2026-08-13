import pandas as pd
import matplotlib.pyplot as plt

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    plt.boxplot(df["Attendance"])

    plt.title("Boxplot of attendance")
    plt.xlabel("")
    plt.ylabel("Attendance ")

    plt.show()

if __name__=="__main__":
    main()
    
import pandas as pd
import matplotlib.pyplot as plt
def main():
    Datapath="student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    plt.hist(df["StudyHours"], edgecolor="black", color="green")

    plt.title("Distribution of StudyHours")
    plt.xlabel("No. of students  ")
    plt.ylabel("Study Hours")

    plt.show()

if __name__=="__main__":
    main()
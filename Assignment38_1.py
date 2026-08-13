import pandas as pd
def main():
    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("First 5 records are ")
    print(df.head())
    print("Last 5 records are ")
    print(df.tail())

    print("Total No. of columns and rows are respectively :")
    print(len(df.columns))
    print(len(df.index))


    print("List of column names : ")
    print(list(df.columns))

    print("Data type column : ")
    print(type(df.columns))

if __name__=="__main__":
    main()


import pandas as pd


def main():
    ########################################################
    # Load the data
    ########################################################

    Border="*"*50
    Data={
        "Name":["Amit","Sagar","Pooja"],
        "Math":[85,90,78],
        "Science":[92,88,80],
        "English":[75,85,82]
    }
    df = pd.DataFrame(Data)
    print(Border)
    print("Shape of dataframe is:",df.shape)
    print(Border)
    print("Column of dataframe is :",list(df.columns))
    print(Border)
    print("Data type : ",type(df))
    print(Border)



if __name__=="__main__":
    main()
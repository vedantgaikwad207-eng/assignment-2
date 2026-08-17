import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
def main():
    ########################################################
    # Load The Data
    ########################################################

    Border="*"*50
    Data={
        "Name":["Amit","Sagar","Pooja"],
        "Math":[85,90,78],
        "Science":[92,88,80],
        "English":[75,85,82],
        
    }
    print(Border)
    df=pd.DataFrame(Data)
    print("Dataframe is :")
    print(df)
    print(Border)
    ########################################################
    # Performing the Min Max scaling
    ########################################################

    scalar=MinMaxScaler()
    df["Math"]=scalar.fit_transform(df[["Math"]])
    print("After minmax scaling ")
    print(df)
    print(Border)
    


if __name__=="__main__":
    main()
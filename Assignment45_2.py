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
    print(Border)
    ########################################################
    # Encoding the Gender column 
    ########################################################

    df["Gender"]=["Male","Male","Female"]
    
    print("Before encoding :")
    print(df)
    print(Border)
    print("After encoding :")
    df_encoded=pd.get_dummies(df,columns=["Gender"])
    print(df_encoded)
    print(Border)
    


if __name__=="__main__":
    main()
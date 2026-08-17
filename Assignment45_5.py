import pandas as pd
import numpy as np
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
    # Encoding the Gender Column
    ########################################################

    df["Gender"]=["Male","Male","Female"]
    print("Before encoding :")
    print(df)
    print(Border)

    print("After encoding :")
    df_encoded=pd.get_dummies(df,columns=["Gender"])
    print(df_encoded)
    print(Border)
    ########################################################
    # Calculating average by grouping male and Female
    ########################################################

    average_marks=df.groupby("Gender")[["Math","Science","English"]].mean()
    print("Average marks according to gender are : \n ",average_marks)
    print(Border)
    ########################################################
    # Graphical Representation
    ########################################################


    print("Graphical representation of sagar vs marks is : ")
    dfa=df.set_index("Name")
    sagar_marks=dfa.loc["Sagar"].drop("Gender")
    sagar_marks.plot(kind="line",marker="o",title="Sagar marks ")
    plt.show()
    print(Border)

    ########################################################
    # Adding Status column 
    ########################################################

    df["Total"]=df["Math"]+df["Science"]+df["English"]

    df["Status"]=np.where(df["Total"]>250,"Pass","Fail")
    print("After adding status column : ")
    print(df)
    print(Border)


if __name__=="__main__":
    main()
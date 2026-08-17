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
    # Adding Status column 
    ########################################################

    df["Total"]=df["Math"]+df["Science"]+df["English"]

    df["Status"]=np.where(df["Total"]>250,"Pass","Fail")
    print("After adding status column : ")
    print(df)
    print(Border)

    ########################################################
    # Boxplot for English Marks 
    ########################################################
    plt.figure(figsize=(8,6))
    plt.boxplot(df["English"],
                label="English marks"
                
                )
    plt.ylabel("English marks")
    plt.legend()
    plt.grid(True)
    plt.show()
    ########################################################
    # End of program 
    ########################################################
    

if __name__=="__main__":
    main()
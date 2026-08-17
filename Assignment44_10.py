import pandas as pd
import matplotlib.pyplot as plt

def main():
    Border="*"*50
    Data={
        "Name":["Amit","Sagar","Pooja"],
        "Math":[85,90,78],
        "Science":[92,88,80],
        "English":[75,85,82],
        
    }

    df = pd.DataFrame(Data)
    print(Border)
    print("Shape of dataframe is:",df.shape)
    print(Border)

    print("Column of dataframe is :",list(df.columns))
    print(Border)
    print("Data type : ",type(df))
    print(Border)

    print("Description is :")
    print(df.describe())
    print(Border)

    df["Total"]=df["Math"]+df["Science"]+df["English"]
    print("New column named Total is :\n ", df["Total"])

    print(Border)

    print("Marks greater than 85 in science are : ")
    print(df[df["Science"]>85])
    print(Border)

    df["Name"]=df["Name"].replace({"Pooja":"Puja"})
    print("Pooja Name changed ")
    print(list(df["Name"]))
    print(Border)


    print("Sorted Data is : ")
    sorted_data=df.sort_values(by="Total",ascending=False)
    print(sorted_data)
    print(Border)


    print("Graph representation is : ")
    print("Student name Vs Total marks ")
    plt.figure(figsize=(8,6))
    plt.bar(df["Name"],df["Total"])
    plt.xlabel("Student Name ")
    plt.ylabel("Total marks ")
    plt.grid(True)

    plt.show()
    print(Border)


    print("Amit Vs Marks")
    dfA=df.set_index("Name")
    amit_data=dfA.loc["Amit"]
    amit_data.plot(kind="line",marker="o",title="Amit Data")
    plt.show()
    print(Border)
    ########################################################
    # Droping the English column from Dataframe 
    ########################################################

    New_df=df.drop(columns=["English"])
    print("New dataframe is : ")
    print(New_df)
    print(Border)
    

if __name__=="__main__":
    main()
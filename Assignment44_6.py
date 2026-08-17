import pandas as pd


def main():
    ########################################################
        # Load the Data
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
    ########################################################
        # Description of Data frame
    ########################################################
    print("Description is :")
    print(df.describe())
    print(Border)
    ########################################################
        # Adding new Column
    ########################################################


    df["Total"]=df["Math"]+df["Science"]+df["English"]
    print("New column named Total is :\n ", df["Total"])

    print(Border)
    ########################################################
        # Displaying marks greater than 85 in science
    ########################################################


    print("Marks greater than 85 in science are : ")
    print(df[df["Science"]>85])
    print(Border)
    ########################################################
        # Replacing the Name : pooja in column "Name"
    ########################################################


    df["Name"]=df["Name"].replace({"Pooja":"Puja"})
    print("Pooja Name changed ")
    print(list(df["Name"]))
    print(Border)
    ########################################################
        # Sorting Data in descending order
    ########################################################

    print("Sorted Data is : ")
    df=df.sort_values(by="Total",ascending=False)
    print(df)
    print(Border)
    
if __name__=="__main__":
    main()
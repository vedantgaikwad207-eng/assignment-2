from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def main():
    Border = "*"*50
################################################
#  Step 1 : Load the Data
################################################
    print(Border)
    print("Step 1 : Load the Data")
    print(Border)

    Datapath = "WinePredictor.csv"

    df=pd.read_csv(Datapath)
    print("First 5 info is : ")
    print(df.head())

    print(Border)

##################################################
#   Step 2 : Clean the dataset   
##################################################
    print(Border)
    print("Step 2 : Clean the dataset")
    print(Border)


    df.dropna(inplace=True)
    print("Dataset is cleaned ")

###################################################
# Step 3 : Spliting of independent and dependent variables
###################################################
    print(Border)
    print("Step 3 : Spliting of independent and dependent variables")
    print(Border)

    X= df.drop(columns=["Class"])
    Y=df["Class"]

    print("Independent varibales : ",X.shape)
    print("Dependent Variables : ",Y.shape)

####################################################
#  Step 4 : Split the dataset 
####################################################
    print(Border)
    print(" Step 4 : Split the dataset")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test :",X_test.shape)
    print("Shape of Y_train :",Y_train.shape)
    print("Shape of Y_test :",Y_test.shape)

    print(Border)


#####################################################
#  Step 5 : Feature scaling
#####################################################
    print(Border)
    print("Step 5 : Feature scaling")
    print(Border)

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)
    print("Feature scaling done ")
    print(Border)

#####################################################
#   Step 6 : Hyperparameter Tuning
#####################################################
    print(Border)
    print("Step 6 : Hyperparameter Tuning")
    print(Border)
    K_values = range(1,21)
    accuracy_scores=[]

    for k in K_values:
        model=KNeighborsClassifier(n_neighbors=k)
        model=model.fit(X_train_scaled,Y_train)
        Y_pred=model.predict(X_test_scaled)
        accuracy=accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)
    print("Accuracy scores are : ")

    for i in accuracy_scores:
        print(i*100)
    print(Border)

########################################################
#  Step 7 : Graphical Representation
########################################################
    print(Border)
    print("Step 7 : Graphical Representation")
    print(Border)


    plt.figure(figsize=(8,6))
    plt.plot(K_values , accuracy_scores,marker="o")
    plt.title("K_Values Vs Accuracy scores ")
    plt.xlabel("K_values")
    plt.ylabel("Accuracy scores ")
    plt.grid(True)
    plt.show()

    print("Graphical Representation done ")
    print("Thank you ")









if __name__=="__main__":
    main()
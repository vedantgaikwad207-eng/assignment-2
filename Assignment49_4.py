from sklearn.preprocessing import StandardScaler,MinMaxScaler
import numpy as np 
import pandas as pd
def EUC(X,Y):
    i=0

    Ans=(X[i]-Y[i])**2 + (X[i+1]-Y[i+1])**2
    return np.sqrt(Ans)

def main():
    X=[[25,2]]
    print("Before feature scaling :")
    print(X)
    Y=[[20,1]]
    q=[]
    for i in X:
        for j in Y:
            L=EUC(i,j)  
            c=[]
            c.append(L)
        q.append(c)
    print("EUC distance is :")
    print(q)   
    scalar=MinMaxScaler()
    X=scalar.fit_transform(X)
    Y=scalar.fit_transform(Y)
    print("After feature scaling : ")
          
    print(X)
    print(Y)
    q=[]
    for i in X:
        for j in Y:
            L=EUC(i,j)  
            c=[]
            c.append(L)
        q.append(c)
    print("EUC distance is :")
    print(q)

if __name__=="__main__":
    main()
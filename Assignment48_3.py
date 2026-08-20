import numpy as np
import matplotlib.pyplot as plt 
def SLR():
    Border="*"*50
    ######################################################################
    # Load the Data 
    ######################################################################

    X=[1,2,3,4,5]
    Y=[20000,25000,30000,35000,40000]
    print(Border)
    print("Independent variable :",X)
    print("Dependent variable :",Y)
    print(Border)
    ######################################################################
    # Calculation 
    ######################################################################

    X_bar=0
    Y_bar=0
    for i in X:
        X_bar=X_bar+i
    X_bar=X_bar/len(X)
    for i in Y :
        Y_bar=Y_bar+i
    Y_bar=Y_bar/len(Y)
    print(Border)

    print("Mean of Independent variable is :",X_bar)

    print("Mean of dependent variable is :",Y_bar)
    print(Border)

    numerator=0
    denominator=0
    for i in range(len(X)):
        numerator=numerator+(X[i]-X_bar)*(Y[i]-Y_bar)
        denominator=denominator+(X[i]-X_bar)**2

    m=1
    m=numerator/denominator
    print("Coefficient of regression is :",m)

    c=0
    c=Y_bar-(m*X_bar)
    print("Intercept is :",c)
    print(Border)

    print("Regression Equation is :")
    print(f"Y={m}*X+{c}")
    print(Border)

    ##############################################################################
    # Prediction 
    ##############################################################################
    Y_pred=0
    Y_pred=m*6+c
    print("Predicted Salary of 6 years of experience is : ",Y_pred)


    ##############################################################################
    # Plotting the Graph 
    ##############################################################################
    n=len(X)
    x=np.linspace(1,6,n)
    y=c+m*x
    plt.plot(x,y,label="Regression line ")
    plt.scatter(X,Y)
    plt.legend()
    plt.grid(True)
    plt.show()
    




def main():
   SLR() 


if __name__=="__main__":
    main()


def SLR():
    Border="*"*50
    ######################################################################
    # Load the Data 
    ######################################################################

    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]
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
    #######################################################################
    # prediction 
    ######################################################################

    Y_pred=[]
    for i in range(len(X)):
        Y_pre=0
        Y_pre=m*X[i]+c
        Y_pred.append(Y_pre)
    print("Predicted answer is ")
    print(Y_pred)
    print("Actual answer is :")
    print(Y)
    ######################################################################
    # Evaluate the model
    ######################################################################
    MSE=0
    for i in range(len(Y)):
        MSE=MSE+(Y[i]-Y_pred[i])**2
    MSE=MSE/len(Y)
    print("Mean squared error is :",MSE)
    SS_res=0
    for i in range(len(Y)):
        SS_res=SS_res+(Y[i]-Y_pred[i])**2
    SS_tot=0
    for i in range(len(Y)):
        SS_tot=SS_tot+(Y[i]-Y_bar)**2
    R2=0
    R2=1-(SS_res/SS_tot)
    print("R-squared value is :",R2)

    print(Border)






def main():
    SLR()

    

if __name__=="__main__":
    main()
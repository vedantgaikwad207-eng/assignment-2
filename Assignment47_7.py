import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def main():
    StudyHours=np.array([[1],[2],[3],[4],[5]])
    Marks=np.array([50,55,60,65,70])
    X=StudyHours
    Y=Marks
    predict=[[6]]
    model=LinearRegression()
    model=model.fit(X,Y)
    Y_pred=model.predict(predict)

    print("Coefficient is :",model.coef_)
    print("Intercept is :",model.intercept_)

if __name__=="__main__":
    main()
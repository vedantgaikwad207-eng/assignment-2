import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def main():
    StudyHours=np.array([[1,7],[2,6],[3,7],[4,6],[5,8]])
    Marks=np.array([50,55,60,65,70])
    
    
    predict=[[6,7]]
    model=LinearRegression()
    model=model.fit(StudyHours,Marks)
    Y_pred=model.predict(predict)
    print("Predicted value is :",Y_pred)
    print("Coefficient is :",model.coef_)
    print("Intercept is :",model.intercept_)

if __name__=="__main__":
    main()
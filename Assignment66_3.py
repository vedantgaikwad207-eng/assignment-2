import numpy as np

def MSE():
    Y=[3,4,5,6]
    Y_bar=[2.5,3.6,5.1,6.2]

    n=4
    sum=0
    for i in range(n):
        sum=sum+(Y[i]-Y_bar[i])

    print("Mean squared error : ",sum)

def BCE():
    y=[1,0]
    p=[0.78,0.34]
    loss=0
    for i in range(2):
        loss = -(y[i]*np.log(p[i])+(1-y[i])*(np.log(1-p[i])))
        if(i==0):

            print(i+1,"Binary cross entropy with class 1 (true): ",loss)
        else:
            print(i+1,"Binary cross entropy with class 0 (False): ",loss)

def main():
    MSE()
    BCE()

if __name__=="__main__":
    main()




    


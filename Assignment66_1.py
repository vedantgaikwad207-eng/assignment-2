import numpy as np 

def sigmoid(z):
    return 1/(1+np.exp(z))

def main():
    x1=2
    x2=3
    w1=0.4
    w2=0.6
    bias=0.5
    z=x1*w1 + x2*w2 + bias 

    print("Weighted sum is : ",z)
    y=sigmoid(z)
    print("Final output : ",y)
    if(y<=0.5):
        print("The output is close to zero ")
    else:
        print("The output is not close to zero ")

if __name__=="__main__":
    main()


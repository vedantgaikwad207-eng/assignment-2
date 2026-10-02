import numpy as np 
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1/(1+np.exp(z))

def ReLU(z):
    return max(0,z)

def Tanh(z):
    return (np.exp(z)-np.exp(-z))/ (np.exp(z)+np.exp(-z))

def main():
    print("The Value should be from range -10 to 10 : ")
    x1=float(input("Enter the first input : "))
    w1=float(input("Enter the first weight : "))
    bias = float(input("Enter the bias value : "))

    z= x1*w1 + bias 
    sig=sigmoid(z)
    re=ReLU(z)
    tan=Tanh(z)
    x=1.0
    plt.figure(figsize=(10,8))
    plt.scatter(x,sig, label="Sigmoid ",color="blue")
    plt.scatter(x,re, label="ReLU",color="green")
    plt.scatter(x,tan, label="Tanh",color="red")

    plt.legend()

    plt.grid(True)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Activation Functions ")
    plt.show()


if __name__=="__main__":
    main()




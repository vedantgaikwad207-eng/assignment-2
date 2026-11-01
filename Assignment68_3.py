import numpy as np

def main():

    matrix = [
        [6,4],
        [8,6]
    ]
    flatten_output=[]
    for row in range(2):
        for col in range(2):
            flatten_output.append(matrix[row][col])
    print(f"Flatten_output = {flatten_output}")

    weight = [0.5,1,0,-0.5]
    
    bias = 1.0
    sum=0
    for i in range(4):
        sum=weight[i]*flatten_output[i]+sum
    sum=sum+bias
    print(f"Output after linear function  : {sum}")
    t=np.tanh(sum)
    print(f"After activation function : {t}")

    def sigmoid(z):
        return 1/(1+np.exp(z))
    
    if (sigmoid(t)==1):
        print(f"Output : 1")
    else: 
        print(f"Output : 0")
        
if __name__=="__main__":
    main()
import numpy as np 



def main():
    print("---------Initializing inputs------------ ")
    inputs=np.array([2.0,1.5])
    weights=np.array([0.5,-0.4])
    bias=0.1
    learning_rate=0.1
    target=1.0

    print(f"Inputs : {inputs}")
    print(f"weights : {weights}")
    print(f"Bias : {bias}")
    print(f" learning rate : {learning_rate}")
    print(f"target output : {target}")

    # Calculation Prediction (Forward Pass )
    # Linear combination : z= weights*inputs + bias
    print("---------Calculation(Forward pass)-----------")
    prediction=np.dot(inputs,weights)+bias
    print("Predicted output : ",prediction)

    # Calculation error & loss
    # error = prediction - target 
    # loss= mean squared error : (1/n)*(error**2) , where n=no. of inputs , error = predicted(Y_pred) - target(Y)
    print("------------Error analysis--------------")
    error = prediction - target
    n=len(inputs)
    loss=(1/n)*(error**2)
    print("Prediction error : ", error)
    print("Loss : ",loss)

    # Update weight using gradient descent logic
    # Partial derivatives (Gradient)
    # dloss/dWeight=(prediction-target)*input
    # dloss/dbias=(prediction-target)
    print("------------------Gradient Descent logic-------------------------")
    weight_gradient=(prediction-target)*inputs
    bias_gradient=error

    old_weight=weights.copy()
    old_bias=bias

    # Weight Update formula :
    # new_Weight=old_weight - (learning_rate*weight_gradient)
    # new_bias=old_bias- (learning_rate*bias_gradient)
    
    new_Weight=old_weight - (learning_rate*weight_gradient)
    new_bias=old_bias- (learning_rate*bias_gradient)
    
    
    # Comparison of weights and bias 

    print("Comparison ")
    print(f"Old weight : {old_weight}")
    print(f"New weight : {new_Weight}")
    print(f"Old Bias : {old_bias}")
    print(f"New bias : {new_bias}")




if __name__=="__main__":
    main()
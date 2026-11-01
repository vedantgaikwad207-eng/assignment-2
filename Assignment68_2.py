def main():
    feature_map=[
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3]
    ]
    def ReLU(z):
        return max(0,z)
    relu_output=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    # Applying ReLU 
    for row in range(3):
        for col in range(3):
            relu_output[row][col]=ReLU(feature_map[row][col])


    # Max Pooling 
    pooled_max=[
        [0,0],
        [0,0]
    ]
    
    for row in range(2):
        for col in range(2):
            top_left = relu_output[row][col]
            top_right=relu_output[row][col+1]
            bottom_left=relu_output[row+1][col]
            bottom_right=relu_output[row+1][col+1]
            high = max(top_left,top_right,bottom_left,bottom_right)
            pooled_max[row][col]=high

    print("RelU output : ")
    for r in relu_output:
        print(r)
    print("Pooled_Max Matrix ")
    for r in pooled_max:
        print(r)
        
if __name__=="__main__":
    main()

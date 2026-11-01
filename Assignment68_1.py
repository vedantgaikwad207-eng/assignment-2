import numpy as np


def main():
    image=[
        [0,0,0,0,0],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    kernel=[
        [-1,-1,-1],
        [0,0,0],
        [1,1,1]
    ]
    feature_map = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    for row in range(3):
        for col in range(3):
            print(f"Calculating the region ({row},{col})")
            region_total=0
            for k_row in range(3):
                for k_col in range(3):

                    image_pixel = image[row + k_row][col + k_col]
                    kernel_value=kernel[k_row][k_col]

                    product=image_pixel*kernel_value
                    print(f"Image ({image_pixel}) x Kernel ({kernel_value}) = {product}")

                    region_total+=product
            feature_map[row][col]=region_total
            print(f"Total for region ({row},{col}) : {region_total}")

    print("Final feature map ")
    for r in feature_map:
        print(r)


# Sir AI varun baghitla aahe 
# Ha code kharach kapalat gela 
        
if __name__=="__main__":
    main()


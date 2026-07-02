from functools import reduce 

def main():
    A=[]
    x=int(input("Enter the No of elements in list : "))
    print("Enter the elements in the lists :")
    for no in range(x):
        x=int(input())
        A.append(x)
    
    smallest = lambda x,y : x if x<y else y
    squa = reduce(smallest,A)
    print("The smallest No is :", squa)
    

if __name__=="__main__":
    main()
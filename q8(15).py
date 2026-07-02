def main():
    A=[]
    x=int(input("Enter the length of the list : "))
    print("Enter the elements : ")
    for i in range(x):
        x=int(input())
        A.append(x)
    div= lambda x : x%3==0 and x%5==0

    squa = list(filter(div, A))
    print("The No. divisible by 3 and 5 are :", squa)
    

if __name__=="__main__":
    main()
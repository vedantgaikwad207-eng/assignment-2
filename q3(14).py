def main():
    x=int(input("Enter the first No. :"))
    y=int(input("Enter the second No. :"))

    greater= lambda x,y :x if x>y else y

    print("The greater no. is :", greater(x,y))
     

if __name__=="__main__":
    main()


    ## if(x>y):
    # print()
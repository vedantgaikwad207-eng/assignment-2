def main():
    x=int(input("Enter the First No :"))
    y=int(input("Enter the second no. :"))

    smallest=lambda x,y: x if x<y else y

    print("The smallest no. is :", smallest(x,y))
    
if __name__=="__main__":
    main()
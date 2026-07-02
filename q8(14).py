def main():
    x=int(input("Enter the first no. :"))
    y=int(input("Enter the Second no. :"))

    add= lambda x,y : x+y

    print(add(x,y))
    

if __name__=="__main__":
    main()
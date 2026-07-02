def main():
    
    print("Enter three no. :")
    x=int(input())
    y=int(input())
    z=int(input())

    greater=lambda x,y,z : x if x>y and x>z  else y if y>x and y>z else z

    print(greater(x,y,z))


if __name__=="__main__":
    main()
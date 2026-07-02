def main():

    print("Enter the No. :")
    x=int(input())
    if(x%3==0 and x%5==0):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5 ")

if (__name__=="__main__"):
    main()

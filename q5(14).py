def main():
    x=int(input("Enter the No. :"))

    fan=lambda x : True if x%2==0 else False

    print(fan(x))


if __name__=="__main__":
    main()
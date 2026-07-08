import threading
def Even():
    for i in range(0,11,2):
        print(i ," ",end="")
def Odd():
    for i in range(1,10,2):
        print(i, " ", end="")


def main():
    Ret = threading.Thread(target=Even )
    Ret.start()
    Ret = threading.Thread(target = Odd)
    Ret.start()

if __name__=="__main__":
    main()
        
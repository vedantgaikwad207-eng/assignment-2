import threading 
def display():
    for i in range(2,22,2):
        print(i," ", end="")

def main():
    t1=threading.Thread(target=display)
    t1.start()




if __name__=="__main__":
    main()
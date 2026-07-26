import psutil
import os
import sys
import schedule
import time 

def display():
    listprocess=[]
    for process in psutil.process_iter():
        info = process.as_dict(attrs=("pid","name","username"))
        listprocess.append(info)

    fobj=open("ProcInfo","w")
    for Data in listprocess :
        fobj.write("\n \n  PID is : %s"%Data.get("pid"))
        fobj.write("  Name is : %s"%Data.get("name"))
        fobj.write("  Username is : %s "%Data.get("username"))


    
def main():
    display()
    
if __name__=="__main__":
    main()
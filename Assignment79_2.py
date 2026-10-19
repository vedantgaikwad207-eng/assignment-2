import tkinter as tk 

root = tk.Tk()

root.title("Maximum from two no.")
root.geometry("300x200")

tk.Label(text="Enter the first no. : ",font=("Arial",14,"bold")).pack()
entry1 =tk.Entry(root)
entry1.pack()

tk.Label(text="Enter the second no. : ",font=("Arial",14,"bold")).pack()
entry2 =tk.Entry(root)
entry2.pack()

def check():
    a=int(entry1.get())
    b=int(entry2.get())
    if(a>b):
        labelResult.config(text="Maximum no. is :"+str(a))
    elif(b>a):
        labelResult.config(text="Maximum no. is :"+str(b))
    else : 
        labelResult.config(text="Both are equal ")

tk.Button(root,text="Find Maximum",font=("Arial",15,"bold"),command=check).pack()

labelResult = tk.Label(root , text="",font=("Arial",10,"bold"))
labelResult.pack()


root.mainloop()


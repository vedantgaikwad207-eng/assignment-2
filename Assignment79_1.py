import tkinter as tk 

root = tk.Tk()

root.title("Addition of two no.")
root.geometry("300x200")

tk.Label(text="Enter the first no. : ",font=("Arial",14,"bold")).pack()
entry1 =tk.Entry(root)
entry1.pack()

tk.Label(text="Enter the second no. : ",font=("Arial",14,"bold")).pack()
entry2 =tk.Entry(root)
entry2.pack()

def add():
    a=int(entry1.get())
    b=int(entry2.get())
    result=a+b
    labelResult.config(text="Addition is :"+str(result))

tk.Button(root,text="Addition",font=("Arial",15,"bold"),command=add).pack()

labelResult = tk.Label(root , text="",font=("Arial",15,"bold"))
labelResult.pack()


root.mainloop()


import tkinter as tk 

# Predefined the values of username and password
username = "XYZ"
password = "XYZ@123"

# code for logic form 
root = tk.Tk()

root.title("Addition of two no.")
root.geometry("300x300")

tk.Label(text="Username",font=("Arial",15)).pack()
entry1 =tk.Entry(root)
entry1.pack()

tk.Label(text="Password ",font=("Arial",15)).pack()
entry2 =tk.Entry(root)
entry2.pack()

def check():
    a=entry1.get()
    b=entry2.get()
    if(a==username and b==password):
        labelResult.config(text="Success")
    else : 
        labelResult.config(text="Failure")

tk.Button(root,text="Login",font=("Arial",15),command=check).pack()

labelResult = tk.Label(root , text="",font=("Arial",15))
labelResult.pack()


root.mainloop()


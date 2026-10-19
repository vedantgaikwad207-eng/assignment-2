import tkinter as tk 

root = tk.Tk()

root.title("Checking eligibility to vote ")
root.geometry("400x200")

tk.Label(text="Name of person : ",font=("Arial",14,"bold")).pack()
entry1 =tk.Entry(root)
entry1.pack()

tk.Label(text="Age : ",font=("Arial",14,"bold")).pack()
entry2 =tk.Entry(root)
entry2.pack()

def check():
    a=entry1.get()
    b=int(entry2.get())
    if(b>=18):
        labelResult.config(text=f"Name of person : {a} \n Eligibility : Eligible")
    else : 
        labelResult.config(text=f"Name of person : {a} \n Eligibility : Not Eligible")

tk.Button(root,text="Check Eligibility ",font=("Arial",15,"bold"),command=check).pack()

labelResult = tk.Label(root , text="",font=("Arial",15,"bold"))
labelResult.pack()


root.mainloop()


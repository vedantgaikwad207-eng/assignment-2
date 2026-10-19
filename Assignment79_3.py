import tkinter as tk 

root = tk.Tk()

root.title("Area of circle")
root.geometry("400x200")

tk.Label(text="Enter the radius of circle : ",font=("Arial",15,"bold")).pack()
entry1 =tk.Entry(root)
entry1.pack()


def area():
    a=int(entry1.get())
    result = 3.14*a*a
    labelResult.config(text="Area of circle is :"+str(result))

tk.Button(root,text="Calculate Area ",font=("Arial",15,"bold"),command=area).pack()

labelResult = tk.Label(root , text="",font=("Arial",15,"bold"))
labelResult.pack()


root.mainloop()


from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Simple Interest Calculator")
root.configure(bg="#f3e6df")

heading = Label(root, text="Simple Interest Calculator", bg="#f3e6df", font=("Calibri", 15), fg="black")
heading.place(x=70, y=20)

principle_label = Label(root, text="Amount of Money", bg="#f3e6df", font=("Calibri", 12), fg="black")
principle_label.place(x=20, y=90)

principle_entry = Entry(root, text="", bd=2, width=22)
principle_entry.place(x=160, y=90)

interest_rate = Label(root, text="Interest Rate", bg="#f3e6df", font=("Calibri", 12), fg="black")
interest_rate.place(x=20, y=130)

interest_entry = Entry(root, text="", bd=2, width=22)
interest_entry.place(x=160, y=130)

time_label = Label(root, text="Time", bg="#f3e6df", font=("Calibri", 12), fg="black")
time_label.place(x=20, y=170)

time_entry = Entry(root, text="", bd=2, width=22)
time_entry.place(x=160, y=170)

def calculate_interest():
    principle = float(principle_entry.get())
    rate = float(interest_entry.get())
    time = float(time_entry.get())
    i = (principle*rate*time)/100
    interest = round(i, 2) # rounding to second decimal place value

    result_label.destroy()
    msg = "Your simple interest is " + str(interest)
    output = Label(root, text=msg, bg="#f3e6df", width=32, font=("Calibri", 12))
    output.place(x=20, y=320)


btn = Button(root, text="Calculate Interest", bg="#b58171", fg="black", font=("Calibri", 15), bd=4, command=calculate_interest)
btn.place(x=50, y=230)

result_frame = LabelFrame(root, text="Result", bg = "#f3e6df", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame, text=" ", bg = "#f3e6df", font=("Calibri", 12), width=33)
result_label.place(x=20, y=20)
result_label.pack()

root.mainloop()
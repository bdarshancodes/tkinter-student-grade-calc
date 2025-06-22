import tkinter as tk
root=tk.Tk()
root.title("studemt data recorder")
root.geometry("800x600")

Total=0


def calculate_sum():
    global Total
    try:
        Total=int(entry2.get())+int(entry3.get())+int(entry4.get())+int(entry5.get())
        result_label.config(text=f"Hello,{entry1.get()} your total obtain  marks are: {Total}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def calculate_percentages():
    try:
        percentage= ( Total / 400) * 100

        if percentage >= 90:
            grade = "A+"
            
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "F"
        result_label1.config(text=f"Dear {entry1.get()} you got {percentage:.2f}%! and your grade is :'{grade}'! ")

    except ValueError:
        result_label1.config(text="please calculate total first")
 

    
    

label1=tk.Label(root,bg="green",bd=5,text=" student name")
label1.pack(pady=5)
entry1=tk.Entry(root,bg="light yellow")
entry1.pack(padx=5,pady=5)
label2=tk.Label(root,bg="green",bd=5,text="subject1")
label2.pack(pady=5)
entry2=tk.Entry(root,bg="light green")
entry2.pack(padx=5,pady=5)
label3=tk.Label(root,bg="green",bd=5,text=" sbject2")
label3.pack(pady=5)
entry3=tk.Entry(root,bg="light green")
entry3.pack(padx=5,pady=5)
label4=tk.Label(root,bg="green",bd=5,text=" subject3")
label4.pack(pady=5)
entry4=tk.Entry(root,bg="light green")
entry4.pack(padx=5,pady=5)
label5=tk.Label(root,bg="green",bd=5,text=" subject4")
label5.pack(pady=5)
entry5=tk.Entry(root,bg="light green")
entry5.pack(padx=5,pady=5)
btn=tk.Button(root,text="Total",bg="orange",command=calculate_sum)
btn.pack(padx=5,pady=5)
result_label=tk.Label(root,bg="light gray")
result_label.pack(padx=5)

tk.Label(root,text="percentage calculate",bg="skyblue").pack(padx=5)
result_label1=tk.Label(root)
result_label1.pack(padx=5)
btn=tk.Button(root,text="click me",bg="light pink",command=calculate_percentages)
btn.pack(padx=5)

root.mainloop()
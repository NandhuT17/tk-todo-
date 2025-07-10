import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("To-Do")
window.config(padx=30,pady=20)
selected_value = tk.StringVar()
drop_down = ttk.Combobox(window,textvariable=selected_value)
drop_down['values'] = ("Add","Remove","Show Tasks")
drop_down.grid(padx=10,pady=10)
drop_down.current(2)


#func to  add or remove
def addorrem():
    choice = selected_value.get()
    item = value.get()
    if choice == "Add" :
        with open("TO-do.txt","a") as f :
            f.write(item + "\n")
        messagebox.showinfo(message="The tasks has been successfully added!! ", title="Task added")
    elif choice == "Remove" :
        try :
            with open("To-do.txt","r") as f :
                lines = f.readlines()
            new_data = [line.strip() for line in lines if line.strip("\n") != item]
            if len(new_data) == len(lines) :
                messagebox.showinfo(message="No values had been found",title="No value Found")
            else:
                with open("To-do.txt","w") as f :
                    f.writelines(new_data)
                messagebox.showinfo(message="The  task had been succesfully removed", title="Task removed")
        except FileNotFoundError :
            messagebox.showerror(message="No such file exists",title="Warning")
    elif choice == "Show Tasks" :
        with open("To-do.txt","r") as f :
            data = f.readlines()
        messagebox.showinfo(message=data)

value = tk.Entry()
value.grid(row=1,column=0)
add_button = tk.Button(window ,text="OK", command=addorrem)
add_button.grid(padx=10,pady=10)


window.mainloop()
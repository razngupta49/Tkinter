import tkinter
from tkinter import BOTH, END

# Main Window
root = tkinter.Tk()
root.title("Window")
# Adding icon
root.iconbitmap("images\icon.ico")
# Size of Window  
root.geometry("500x500")
root.resizable(0,0) 
# Adding Background color Blue
# root.config(bg='blue')

def print():
    text = tkinter.Label(out_frame, text=text_entry.get(), bg='#ff0000').pack()
    text_entry.delete(0, END)

def count(number):
    global value
    text = tkinter.Label(out_frame, text=number, bg='#ff0000').pack()
    value = number+1

# Definig Frame
input_frame = tkinter.Frame(root, bg='#0000ff', width=500, height=100)
out_frame = tkinter.Frame(root, bg='red', width=500, height=400)
input_frame.pack(padx=10, pady=10)
out_frame.pack(padx=10, pady=(0,10))
# Adding Input entry
text_entry = tkinter.Entry(input_frame, width=40)
text_entry.grid(row=0, column=0, padx=5, pady=5)
input_frame.grid_propagate(0)
# Adding Print Button
print_button = tkinter.Button(input_frame, text='Print', command=print)
print_button.grid(row=0, column=1, padx=5, pady=5, ipadx=30)
# fixed the output frame
out_frame.pack_propagate(0)
# Adding count Button and Function count
value = 1
count_button = tkinter.Button(input_frame, text='count',command=lambda:count(value))
count_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='WE')

# MainLoop
root.mainloop()
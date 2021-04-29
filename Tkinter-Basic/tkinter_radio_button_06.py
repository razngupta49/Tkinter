import tkinter
from tkinter import IntVar

# Main Window
root = tkinter.Tk()
root.title("Basic Window")
# Adding icon
root.iconbitmap("images\icon.ico")
# Size of Window
root.geometry("400x300")
root.resizable(0,0)

# Defining the function for print_button

def printthevalue():
    if number.get()==1:
        num_label = tkinter.Label(output_frame, text='one')
    elif number.get()==2:
        num_label = tkinter.Label(output_frame, text='two')
    num_label.pack()
    
# Variable to store the value of radio button
number=IntVar()
# for set default value to radio button
number.set(1)

# Defining frames
input_frame = tkinter.LabelFrame(root, text='testing', width=450, height=150)
output_frame = tkinter.Frame(root, width=450, height=250)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=10)  

# Widgets

radio1 = tkinter.Radiobutton(input_frame, text='one',variable=number, value=1)
radio2 = tkinter.Radiobutton(input_frame, text='two', variable=number, value=2)
print_button = tkinter.Button(input_frame, text='Print', command=printthevalue)

radio1.grid(row=0, column=0, padx=10, pady=10)
radio2.grid(row=0, column=1, padx=10, pady=10)
print_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# MainLoop
root.mainloop()
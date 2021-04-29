import tkinter
from tkinter import BOTH, StringVar, END

# Main Window
root = tkinter.Tk()
root.title('Hello World')
# Adding icon
root.iconbitmap("images\icon.ico")
# Size of Window
root.geometry("400x400")
root.resizable(0,0)
# Adding Background color 
root.config(bg='#242B2E')

# Function Define for submit button
def submit():
    if input_style.get()=='normal':
        name_label = tkinter.Label(output_frame, text='Hello, '+ name.get(), bg='#758283')
    elif input_style.get()=='upper':
        name_label = tkinter.Label(output_frame, text=('Hello, '+ name.get()).upper(), bg='#758283')
    name_label.pack()
    # Clear The input field for next one
    name.delete(0, END)
    
# Define the Frames
input_frame = tkinter.LabelFrame(root, bg='#46B2E0')
output_frame = tkinter.LabelFrame(root, bg='#758283')
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)
# Widgets
name = tkinter.Entry(input_frame, text='Enter Your Name: ', width=20)
submit = tkinter.Button(input_frame, text='Submit', command=submit)
name.grid(row=0, column=0, padx=10, pady=10)
submit.grid(row=0, column=1, padx=10, pady=10, ipadx=20)
# Radio Button
input_style = StringVar()
# set default value of radio button normal
input_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text="Normal", variable=input_style, value='normal', bg='#46B2E0')
upper_button = tkinter.Radiobutton(input_frame, text="Upper", variable=input_style, value='upper', bg='#46B2E0')
normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button.grid(row=1, column=1, padx=2, pady=2)

# MainLoop
root.mainloop()

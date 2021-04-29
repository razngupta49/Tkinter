import tkinter
from tkinter import BOTH

# Main Window
root = tkinter.Tk()
root.title("Window")
# Adding icon
root.iconbitmap("images\icon.ico")
# Size of Window
root.geometry("400x300")
root.resizable(0,0)
# Adding Background color Blue
root.config(bg='blue')

# Create widgets

label1 = tkinter.Label(root, text='This is label one1 ')
label1.pack()

label2 = tkinter.Label(root, text='This is label two2', font=('Arial', 18, 'bold'))
label2.pack()

label3 = tkinter.Label(root, text='This is label three3', font=('Arial', 12), bg='red')
label3.pack(padx=50, pady=10) 

label4 = tkinter.Label(root, text='This is label four4', bg='black', fg='white')
label4.pack(pady=(0,10), ipadx=50, ipady=10, anchor='w') 

label5 = tkinter.Label(root, text='This is label five5', bg='#ffffff', fg='#123456')
label5.pack(fill=BOTH, expand=True, padx=10, pady=10)
 
# MainLoop
root.mainloop()
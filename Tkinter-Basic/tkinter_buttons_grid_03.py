import tkinter

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

button1 = tkinter.Button(root, text='one1')
button1.grid(row=0, column=0)

button2 = tkinter.Button(root, text='two2', bg='cyan')
button2.grid(row=0, column=1)

button3 = tkinter.Button(root, text='three3', bg='red', activebackground='green')
button3.grid(row=0, column=2, ipadx=10)

button4 = tkinter.Button(root, text='four4', bg='black', fg='white')
button4.grid(row=1, column=0, columnspan=3, sticky='WE')


test1 = tkinter.Button(root, text='test1')
test2 = tkinter.Button(root, text='test2')
test3 = tkinter.Button(root, text='test3')
test4 = tkinter.Button(root, text='test4')
test5 = tkinter.Button(root, text='test5')
test6 = tkinter.Button(root, text='test6')

test1.grid(row=2, column=0)
test2.grid(row=2, column=1)
test3.grid(row=2, column=2, sticky='W')
test4.grid(row=3, column=0)
test5.grid(row=3, column=1)
test6.grid(row=3, column=2, sticky='W')

# MainLoop
root.mainloop()
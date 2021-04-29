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
# root.config(bg='blue')

# Define Frame
frame1 = tkinter.Frame(root, bg='red')
frame2 = tkinter.Frame(root, bg='blue')
frame3 = tkinter.LabelFrame(root, text='Label Frame')
# Pack Frame on root Window
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill='x', expand=True)
frame3.pack(fill=BOTH, expand=True)
# Frame1
tkinter.Label(frame1, text='text').pack()
tkinter.Label(frame1, text='text').pack()
tkinter.Label(frame1, text='text').pack()
# Frame2
tkinter.Label(frame2, text='text').grid(row=0, column=0)
tkinter.Label(frame2, text='text').grid(row=1, column=1)
tkinter.Label(frame2, text='text').grid(row=2, column=2)
# Frame3
tkinter.Label(frame3, text='text').grid(row=0, column=0)
# MainLoop
root.mainloop()
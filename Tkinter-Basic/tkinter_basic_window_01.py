import tkinter

# Main Window
root = tkinter.Tk()
root.title("Basic Window")
# Adding icon
root.iconbitmap("images\icon.ico")
# Size of Window
root.geometry("400x300")
root.resizable(0,0)
# Adding Background color Blue
root.config(bg='blue')

# Creating Second Window root1
root1 = tkinter.Toplevel()
root1.title("Second Window")
root1.iconbitmap("images\icon.ico")
root1.geometry("400x300+500+100")
root1.config(bg='red')

# MainLoop
root.mainloop()
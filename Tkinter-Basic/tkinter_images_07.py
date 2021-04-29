import tkinter
from PIL import ImageTk, Image
# Main Window
root = tkinter.Tk()
root.title("Basic Window")
# Adding icon
root.iconbitmap("images\icon.ico")
# Size of Window
root.geometry("400x300")

# Working with Images
# For png file
# First create image
image = tkinter.PhotoImage(file='images\car.png',)
label = tkinter.Label(root, image=image)
label.pack()
# Adding image to the button
button = tkinter.Button(root, image=image)
button.pack()

# For jpg file we use pillow(PIL) library
image2 = ImageTk.PhotoImage(Image.open('images\house.jpg') )
label2 = tkinter.Label(root, image=image2)
label2.pack()

# MainLoop
root.mainloop()
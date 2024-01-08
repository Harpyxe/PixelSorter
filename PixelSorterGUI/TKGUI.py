import os
import sys
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Frame, Label








def initPIC():

    image = Image.open("test.jpg")
    photoimg = ImageTk.PhotoImage(image)
    label = Label(root, image=photoimg).pack(side="left")







while True:
    root = tk.Tk()
    root.title('PixelSorter GUI')
    center_window(600, 600)


    label1 = tk.Label(root, text='dataaa').pack(side="left")


    initPIC()




    root.mainloop()
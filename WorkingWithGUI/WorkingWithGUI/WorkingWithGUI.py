#import tkinter

#top = tkinter.Tk()
##Code to add widgets will go here
#top.mainloop()


#We start by importing the Tkinter module.
from tkinter import *

#To initialize Tkinter, we have to create a Tk root widget. This is an ordinary window,
#with a title bar and other decoration provided by your window manager.
#You should only create one root widget for each program, and it must be created before any other widgets.
root = Tk()

#Next, we create a Label widget as a child to the root window:
w = Label(root, text = "Hello World") #A Label widget can display either text or an icon or other image.
#Next, we call the pack method on this widget. This tells it to size itself to fit the given text, and make itself visible.
w.pack()

#The window won’t appear until we’ve entered the Tkinter event loop:
root.mainloop()
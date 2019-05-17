from tkinter import *


def close_window():
    fen.destroy()

def recupere():
    showinfo("Alerte", entree.get())
	
fen = Tk()

fen.title("Simple GUI")
#fen.geometry("800x600")

label = Label(fen, text="Hello World !")
label.pack()

button = Button(fen, text="Quit", command=fen.destroy)
button.pack()

fen.mainloop()

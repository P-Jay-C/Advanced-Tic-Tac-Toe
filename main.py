from tkinter import messagebox
from tkinter import *

window = Tk()

window.geometry("1350x750+0+0")
window.title("Tic Tac Toe")
window.configure(background="Cadet Blue")

Tops = Frame(window, bg='Cadet Blue', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops,font=("arial",50,'bold'), text='Advanced Tic Tac Toe Game', bd=21, background='Cadet Blue',fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(window, bg='Powder Blue', pady=2, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, background="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, background="Cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, background="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, background="Cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1,column=0)

playerX = IntVar()
playerO = IntVar()

playerX.set(0)
playerO.set(0)

button = StringVar()

lblPlayerX = Label(RightFrame1,font=("arial",40,"bold"), text="Player X:",padx=2,pady=2,bg="Cadet Blue")
lblPlayerX.grid(row=0,column=0,sticky=W)

txtPlayerX = Entry(RightFrame1, font=("Arail",40,"bold"), textvariable= playerX, width=14,bd=2,foreground='black',justify=LEFT)
txtPlayerX.grid(row=0,column=1)

lblPlayerO = Label(RightFrame1,font=("arial",40,"bold"), text="Player O:",padx=2,pady=2,bg="Cadet Blue")
lblPlayerO.grid(row=1,column=0)

txtPlayerO = Entry(RightFrame1, font=("Arail",40,"bold"), textvariable= playerO, width=14,bd=2,foreground='black',justify=LEFT)
txtPlayerO.grid(row=1,column=1)

            # This is for the other buttons
btnReset = Button(RightFrame2, text="Reset", font=("Times", 26, "bold"), height=1, width=12)
btnReset.grid(row=0, column=0,padx=6,pady=10)

btnNewGame = Button(RightFrame2, text="New Game", font=("Times", 26, "bold"), height=1, width=12)
btnNewGame.grid(row=0, column=1,padx=6,pady=11)

button1 = Button(LeftFrame, text=" ", font=("Times", 26, "bold"), height=3, width=8, background="gainsboro")
button1.grid(row=0, column=0,sticky=S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=("Times", 26, "bold"), height=3, width=8, background="gainsboro")
button2.grid(row=0, column=1,sticky=S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=("Times", 26, "bold"), height=3, width=8, background="gainsboro")
button3.grid(row=0, column=2,sticky=S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=("Times", 26, "bold"), height=3, width=8, background="gainsboro")
button4.grid(row=1, column=0,sticky=S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=("Times", 26, "bold"), height=3, width=8, background="gainsboro")
button5.grid(row=1, column=1,sticky=S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=("Times", 26, "bold"), height=3, width=8, background="gainsboro")
button6.grid(row=1, column=2,sticky=S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=("Times", 26, "bold"), height=3, width=8, background="gainsboro")
button7.grid(row=2, column=0,sticky=S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=("Times", 26, "bold"), height=3, width=8, background="gainsboro")
button8.grid(row=2, column=1,sticky=S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=("Times", 26, "bold"), height=3, width=8, background="gainsboro")
button9.grid(row=2, column=2,sticky=S+N+E+W)

window.mainloop()


















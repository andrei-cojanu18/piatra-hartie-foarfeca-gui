from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('piatra-hartie-foarfeca')


def schimbare(nr):
    if nr == 1:
        return 'piatra'
    elif nr == 2:
        return 'hartie'
    elif nr == 3:
        return 'foarfeca'


def hartie_press(event):
    AI_player = random.randint(1, 3)
    AI_player = schimbare(AI_player)
    player = 'hartie'
    if player.lower() == AI_player:
        messagebox.showinfo("Este egalitate", "Calculatorul a ales " + AI_player + " iar tu ai ales " + player)
    elif player.lower() == 'hartie' and AI_player == 'piatra':
        messagebox.showwarning("Ai castigat", "Calculatorul a ales " + AI_player + " iar tu ai ales " + player)
    elif player.lower() == 'hartie' and AI_player == 'foarfeca':
        messagebox.showerror("Ai pierdut", "Calculatorul a ales " + AI_player + " iar tu ai ales " + player)

    print('ai apasat hartie')


def piatra_press(event):
    AI_player = random.randint(1, 3)
    AI_player = schimbare(AI_player)
    player = 'piatra'
    if player.lower() == AI_player:
        messagebox.showinfo("Este egalitate", "Calculatorul a ales " + AI_player + " iar tu ai ales " + player)
    elif player.lower() == 'piatra' and AI_player == 'foarfeca':
        messagebox.showwarning("Ai castigat", "Calculatorul a ales " + AI_player + " iar tu ai ales " + player)
    elif player.lower() == 'piatra' and AI_player == 'hartie':
        messagebox.showerror("Ai pierdut", "Calculatorul a ales " + AI_player + " iar tu ai ales " + player)
    print('ai apasat piatra')


def foarfeca_press(event):
    AI_player = random.randint(1, 3)
    AI_player = schimbare(AI_player)
    player = 'foarfeca'
    if player.lower() == AI_player:
        messagebox.showinfo("Este egalitate", "Calculatorul a ales " + AI_player + " iar tu ai ales " + player)
    elif player.lower() == 'foarfeca' and AI_player == 'hartie':
        messagebox.showwarning("Ai castigat", "Calculatorul a ales " + AI_player + " iar tu ai ales " + player)
    elif player.lower() == 'foarfeca' and AI_player == 'piatra':
        messagebox.showerror("Ai pierdut", "Calculatorul a ales " + AI_player + " iar tu ai ales " + player)
    print('ai apasat foarfeca')


for i in range(5):
    root.columnconfigure(i, weight=1, minsize=10)
    root.rowconfigure(i, weight=1, minsize=50)

Label(root, text="piatra-hartie-foarfeca",
      fg='white',
      bg='black'
      ).grid(column=0, row=0)

Button(root, text='Quit', command=root.destroy).grid(column=0, row=4)

hartie = Button(root, text='hartie')
hartie.grid(column=0, row=1)
hartie.bind('<Button-1>', hartie_press)

piatra = Button(root, text='piatra')
piatra.grid(column=0, row=2)
piatra.bind('<Button-1>', piatra_press)

foarfeca = Button(root, text='foarfeca')
foarfeca.grid(column=0, row=3)
foarfeca.bind('<Button-1>', foarfeca_press)

root.mainloop()

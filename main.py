import tkinter as tk
from tkinter import ttk

import random as rd


DICES = '⚀', '⚁', '⚂', '⚃', '⚄', '⚅'


def main():
    def do_dice():
        dices = list(DICES)

        try:
            dices.remove(roll.cget('text'))
        except NameError:
            pass

        return rd.choice(dices)

    root = tk.Tk()

    heigh = root.winfo_screenheight()
    roll = ttk.Label(font=(None, int(heigh/4)), text=do_dice())
    roll.pack()
    roll.bind('<Button-1>', lambda _: roll.configure(text=do_dice()))

    root.mainloop()


if __name__ == '__main__':
    main()

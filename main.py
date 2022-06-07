'''
Roll and dice game
'''
import tkinter as tk
from tkinter import ttk
import random as rd

def rolling_dice(roll, dice):
    roll.configure(text=rd.choice(dice))
    roll.pack()

def main():
    '''
    Main game loop
    '''

    window = tk.Tk()
    edge = int(window.winfo_screenheight()/2)
    # window.geometry(str(edge) + 'x' + str(edge))
    window.title('Dicer')

    dice = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

    roll = ttk.Label(window,
                    text=rd.choice(dice),
                    font=('Arial', int(edge/2)))

    play = ttk.Button(window,
                     text='Roll',
                     command=lambda: rolling_dice(roll, dice))

    roll.pack(expand=True)
    play.pack(fill='x')

    window.mainloop()


if __name__ == '__main__':
    main()

'''
Roll and dice game
'''
import tkinter as tk
import random as rd


def main():
    '''
    Main game loop
    '''

    def rolling_dice():
        roll.configure(text=rd.choice(dice))
        roll.pack()

    window = tk.Tk()
    edge = int(window.winfo_screenheight()/2)
    window.geometry(str(edge) + 'x' + str(edge))
    window.title('Dicer')

    dice = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

    roll = tk.Label(window,
                    text=rd.choice(dice),
                    font=('Arial', int(edge/2)))

    play = tk.Button(window,
                     text='Roll',
                     command=rolling_dice)

    close = tk.Button(window,
                      text='Close',
                      command=window.destroy)

    roll.pack(expand=True)
    play.pack(fill='x')
    close.pack(fill='x')

    window.mainloop()


if __name__ == '__main__':
    main()

import tkinter as tk
import random as rd

window = tk.Tk()
edge = int(window.winfo_screenheight()/2)
window.geometry(str(edge) + 'x' + str(edge))
window.title('Dicer')

dice = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

roll = tk.Label(window, text = rd.choice(dice), font = ('Arial', int(edge/2)))
roll.pack(expand = True)

def rolling_dice():
  roll.configure(text = rd.choice(dice))
  roll.pack


play = tk.Button(window, text = 'Roll', command = rolling_dice)
play.pack(fill = 'x')

close = tk.Button(window, text = 'Close', command = window.destroy)
close.pack(fill = 'x')

window.mainloop()


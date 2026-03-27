import tkinter as tk
from lootboxModule import lootbox

loot = lootbox()

window = tk.Tk()

label = tk.Label(window, text=f"{loot}")

window.geometry("500x500")

label.pack()

window.mainloop()
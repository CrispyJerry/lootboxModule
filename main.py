import tkinter as tk
from lootboxModule import *
import time

loot = lootbox("common")

def getLootbox():
    loot = lootbox("common")
    return loot
    
itemRarity = {
    "common" : "black",
    "epic" : "blue",
    "rare" : "purple",
    "legendary" : "red"
}

print(loot)

window = tk.Tk()

label = tk.Label(window, text=f"{loot["item"]}", fg = itemRarity[loot["rarity"]])
label.pack()

def rollLoot():
    loot = getLootbox()
    label.config(text = f"{loot["item"]}",fg = itemRarity[loot["rarity"]])


button = tk.Button(window,text="Open Lootbox",command= rollLoot)
button.pack()
window.geometry("200x200")


window.mainloop()
import tkinter as tk
from lootboxModule import lootbox

loot = lootbox()

itemRarity = {
    "common" : "black",
    "epic" : "blue",
    "rare" : "purple",
    "legendary" : "red"
}

print(loot)

window = tk.Tk()

label = tk.Label(window, text=f"{loot["item"]}", fg = itemRarity[loot["rarity"]])

window.geometry("500x500")

label.pack()

window.mainloop()
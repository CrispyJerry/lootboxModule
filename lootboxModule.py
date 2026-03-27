import random

gameLoot = {
    "common" : ["dagger","metal pipe","knuckle dusters"],
    "rare" : ["machete","pistol","baseball bat"],
    "epic" : ["bolt action","shotgun","chainsaw"],
    "legendary" : ["50 Cal","silenced pistol","Shadow Kunai"]
}

lootboxTypes = {
    "common" : [60,85,97],
    "rare" : [50,75,96],
    "epic": [40,55,95],
    "legendary": [30,50,90]
}

def rarityGenerator():
    x = random.randint(1,100)
    return x
    
def lootGenerator(lootbox):

    lootnum = rarityGenerator()

    print(f'This is lootnum index {lootbox["common"[1]]}')

    # if lootnum < lootbox[1]:
    #     return "common"

    # elif lootnum < lootbox[2]:
    #     return "rare"

    # elif lootnum < lootbox[3]:
    #     return "epic"

    # else:
    #     return "legendary"
    

def lootbox():

    rarity = lootGenerator()
    item = random.choice(gameLoot[rarity])

    loot = {
        "rarity" : rarity,
        "item" : item
    }

    # return f'{rarity.upper()}: {item}'
    return loot


print(lootGenerator("common"))
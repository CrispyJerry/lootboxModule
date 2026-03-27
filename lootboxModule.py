import random

gameLoot = {
    "common" : ["dagger","metal pipe","knuckle dusters"],
    "rare" : ["machete","pistol","baseball bat"],
    "epic" : ["bolt action","shotgun","chainsaw"],
    "legendary" : ["50 Cal","silenced pistol","Shadow Kunai"]
    
}


def rarityGenerator():
    x = random.randint(1,100)
    return x
    
def lootGenerator():
    lootnum = rarityGenerator()

    if lootnum < 60:
        return "common"

    elif lootnum < 85:
        return "rare"
    
    elif lootnum < 97:
        return "epic"
    
    else:
        return "legendary"
    

def lootbox():
    rarity = lootGenerator()
    item = random.choice(gameLoot[rarity])
    return f'{rarity.upper()}: {item}'

for i in range(1000):
    print(lootbox())
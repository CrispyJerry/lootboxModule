import random

gameLoot = {
    "common" : ["dagger","metal pipe","knuckle dusters"],
    "rare" : ["machete","pistol","baseball bat"],
    "epic" : ["bolt action","shotgun","chainsaw"],
    "legendary" : ["50 Cal","silenced pistol","Shadow Kunai"]
}

rarities = ["common","rare","epic","legendary"]

lootboxTypes = {
    "common" : [60,85,97,100],
    "rare" : [50,75,96,100],
    "epic": [30,45,95,100],
    "legendary": [30,50,85,100]
}

def lootGenerator(lootboxName):

    probs = lootboxTypes[lootboxName]
    roll = random.randint(1,100)
    length = len(rarities)
    
    for rarity, threshold in zip(rarities,probs):
        if roll <= threshold:
            return rarity
    
def lootbox(lootboxName):

    rarity = lootGenerator(lootboxName)
    item = random.choice(gameLoot[rarity])

    loot = {
        "rarity" : rarity,
        "item" : item
    }

    return loot
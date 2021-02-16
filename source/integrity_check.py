'''
 Basic QC checks for yaml/data integrity.
 Useful for checking data entry.
'''

from yaml import safe_load

# Expected Values
TOT_COST = 162
CHAMPS = 58
nCosts  = {"one": 13,
           "two": 13,
           "three": 13,
           "four": 11,
           "five": 8}
num_traits = { "Adept":3,
               "Assassin":5,
               "Blacksmith":1,
               "Brawler":7,
               "Cultist":8,
               "Daredevil":1,
               "Divine":6,
               "Dragonsoul":7,
               "Duelist":6,
               "Elderwood":7,
               "Emperor":1,
               "Enlightened":5,
               "Executioner":3,
               "Exile":2,
               "Fabled":3,
               "Fortune":5,
               "Keeper":6,
               "Mage":6,
               "Mystic":5,
               "Ninja":4,
               "Sharpshooter":5,
               "Slayer":5,
               "Spirit":4,
               "Syphoner":4,
               "The Boss":1,
               "Warlord":7,
               "Vanguard":7}

traits  = [ "Adept",
            "Assassin",
            "Blacksmith",
            "Brawler",
            "Cultist",
            "Daredevil",
            "Divine",
            "Dragonsoul",
            "Duelist",
            "Elderwood",
            "Emperor",
            "Enlightened",
            "Executioner",
            "Exile",
            "Fabled",
            "Fortune",
            "Keeper",
            "Mage",
            "Mystic",
            "Ninja",
            "Sharpshooter",
            "Slayer",
            "Spirit",
            "Syphoner",
            "The Boss",
            "Warlord",
            "Vanguard"]

# Load yaml
CHAMPION_DATA = None
with open("../Data/Champions.yaml", 'r') as stream:
    CHAMPION_DATA = safe_load(stream)


# Check the total number of champions
print ("Checking total champions...")
if len(CHAMPION_DATA) == CHAMPS:
    print("Okay!")
else: print ("Error!")

# Check the number of each trait
print ("Checking trait counts....")
cur_traits = {}
for cur_trait in traits:
    cur_traits[cur_trait] = 0
for champion, info in CHAMPION_DATA.items():
    for cur_trait in CHAMPION_DATA[champion]["Traits"]:
        cur_traits[cur_trait] +=1
MATCH = True
for cur_trait in traits:
    if num_traits[cur_trait] != cur_traits[cur_trait]:
        MATCH = False
        print ("Error in "+cur_trait)
if MATCH:
    print ("Okay!")

# Check each cost is filled and each trait >=2
print ("Checking total cost...")
COST = 0
for champion, info in CHAMPION_DATA.items():
    COST += info["Cost"]
if TOT_COST == COST:
    print ("Okay!")
else:
    print ("Error!")

# Check the number of each cost
# Maybe not needed for now...
# Check casing?

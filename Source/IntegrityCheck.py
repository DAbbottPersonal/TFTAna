##############################################
# Basic QC checks for yaml/data integrity!####
##############################################

from yaml import safe_load, dump

# Expected Values
totCost = 162
nChamps = 58
nCosts  = {"one": 13,
           "two": 13,
           "three": 13,
           "four": 11,
           "five": 8}
nTraits = { "Adept":3,
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
champion_data = None
with open("../Data/Champions.yaml", 'r') as stream:
    champion_data = safe_load(stream)


# Check the total number of champions
print ("Checking total champions...")
if len(champion_data) == nChamps: print("Okay!")
else: print ("Error!")

# Check the number of each trait
print ("Checking trait counts....")
cur_traits = {}
for cur_trait in traits: cur_traits[cur_trait] = 0
for champion, info in champion_data.items():
    for cur_trait in champion_data[champion]["Traits"]:
        cur_traits[cur_trait] +=1
isMatch = True
for cur_trait in traits:
    if nTraits[cur_trait] != cur_traits[cur_trait]:
        isMatch = False
        print ("Error in "+ cur_trait)
if isMatch: 
    print ("Okay!")

# Check each cost is filled and each trait >=2
print ("Checking total cost...")
cost = 0
for champion, info in champion_data.items():
    cost += info["Cost"]
if totCost == cost:
    print ("Okay!")
else:
    print ("Error!")

# Check the number of each cost
# Maybe not needed for now...
#matched =
#for cur_cost in ["one","two","three","four","five"]:
    

# Check casing?








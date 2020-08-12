##############################################
# Basic QC checks for yaml/data integrity!####
##############################################

from yaml import safe_load, dump

# Expected Values
totCost = 158
nChamps = 57
nCosts  = {"one": 13,
           "two": 13,
           "three": 13,
           "four": 10,
           "five": 8}
nTraits = { "Astro" : 4,
            "Battlecast" : 6,
            "Blademaster" : 7,
            "Blaster" : 5,
            "Brawler" : 5,
            "Celestial" : 5,
            "Chrono" : 8,
            "Cybernetic" : 7,
            "Dark Star" : 6,
            "Demolitionist" : 3,
            "Infiltrator" : 5,
            "Mana-Reaver" : 3,
            "Mech Pilot" : 3,
            "Mercenary" : 1,
            "Mystic" : 5,
            "Paragon" : 1,
            "Protector" : 5,
            "Rebel" : 7,
            "Sniper" : 5,
            "Sorcerer" : 7,
            "Space Pirate" : 4,
            "Starship" : 1,
            "Star Guardian" : 7,
            "Vanguard" : 6}


traits = [ "Astro",
            "Battlecast",
            "Blademaster",
            "Blaster",
            "Brawler",
            "Celestial",
            "Chrono",
            "Cybernetic",
            "Dark Star",
            "Demolitionist",
            "Infiltrator",
            "Mana-Reaver",
            "Mech Pilot",
            "Mercenary",
            "Mystic",
            "Paragon",
            "Protector",
            "Rebel",
            "Sniper",
            "Sorcerer",
            "Space Pirate",
            "Starship",
            "Star Guardian",
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
        break
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








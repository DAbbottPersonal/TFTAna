#########################################################
# Find the perfect Synergies for a team of two or more! #
#########################################################

from yaml import safe_load, dump

def checkSynergies(check_champs, all_syn, all_champs):
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

    synergy_tally = {}
    synergy_set   = []
    for cur_trait in traits: synergy_tally[cur_trait] = 0
    for cur_champ in check_champs:
        for cur_trait in all_champs[cur_champ]["Traits"]:
            synergy_tally[cur_trait] += 1
            if cur_trait not in synergy_set: synergy_set.append(cur_trait)
    #print (synergy_tally)
    for synergy in synergy_set:
        #print ("Testing synergy: " + synergy)
        #print ("With a tally of: " + str(synergy_tally[synergy]))
        if synergy_tally[synergy] not in all_syn[synergy]: return False

    return True

# Uses test case of Rakan and Xin
def testPass(all_syn, all_champs):
    return checkSynergies(["Rakan","Xin Zhao"], all_syn, all_champs)
    
def testFail(all_syn, all_champs):
    case_1 = checkSynergies(["Rakan","Xin Zhao","Ashe"], all_syn, all_champs)
    case_2 = checkSynergies(["Aurelion Sol"], all_syn, all_champs)
    return (case_1 and case_2)

def run_tests(all_syn, all_champs):
    isPerf = testPass(synergy_data, champion_data)
    if isPerf: print("Perfect synergy test passed!")
    else: print("Perfect synergy test failed...")

    isPerf = testFail(synergy_data, champion_data)
    if isPerf: print("Imperfect synergy test passed!")
    else: print("Imperfect synergy test failed...")

#########################
# Main code begins here #
#########################

# Load data
champion_data = None
with open("../Data/Champions.yaml", 'r') as stream:
    champion_data = safe_load(stream)

synergy_data = None
with open("../Data/Synergies.yaml", 'r') as stream:
    synergy_data = safe_load(stream)

# Run test to make sure simple cases are working
run_tests(synergy_data, champion_data)

# Run combination code



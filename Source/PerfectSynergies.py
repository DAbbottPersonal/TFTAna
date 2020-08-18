#########################################################
# Find the perfect Synergies for a team of two or more! #
#########################################################
import io
from yaml import safe_load, dump
from itertools import product
from itertools import combinations

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

champion_data = None
with open("../Data/Champions.yaml", 'r') as stream:
    champion_data = safe_load(stream)
champ_list = list(champion_data.keys())
synergy_data = None
with open("../Data/Synergies.yaml", 'r') as stream:
    synergy_data = safe_load(stream)


champs_by_level = {"1":[], "2":[], "3":[], "4":[], "5":[], "6":[], "7":[], "8":[], "9":[]}
champs_by_cost  = {"1":[], "2":[], "3":[], "4":[], "5":[]}
costs_at_level  = {"1":3, 
                   "2":3, 
                   "3":3, 
                   "4":3, 
                   "5":4, 
                   "6":4, 
                   "7":5, 
                   "8":5, 
                   "9":5} # 999 is a sentinal value for no limit
 

for champion, info in champion_data.items():
    champs_by_cost[str(info["Cost"])].append(champion)

for level in range(1,10,1):
    i = 1
    while (i<=costs_at_level[str(level)]):
        champs_by_level[str(level)] += champs_by_cost[str(i)]
        i+=1

    #if info["Cost"] <= costs_at_level[str(level)]:
    #    champs_by_level[str(info["Cost"])].append(champion)


total_perf = 0
for level in range(1,8,1):
    print ("Running on level: ",str(level))
    test_list = combinations(champs_by_level[str(level)], level)
    print ("List made")
    perfect_syn = []
    for cur_syn in test_list:
        if checkSynergies(cur_syn, synergy_data, champion_data):
            perfect_syn.append(cur_syn)

    print (str(len(perfect_syn)) + " found!")
    print (perfect_syn)
    total_perf += len(perfect_syn)
    oname = ''.join(["Perfect_level",str(level),".yaml"])
    with io.open(oname, 'w', encoding='utf8') as outfile:
        dump(perfect_syn, outfile, default_flow_style=False, allow_unicode=True)



print ("Total perfect synergies: ", total_perf)

print("Done")

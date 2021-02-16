#########################################################
# Find the perfect Synergies for a team of one or more! #
#########################################################
import io
from argparse import ArgumentParser
from itertools import combinations, product
from yaml import safe_load, dump

def exit_(msg):
    if msg: print (msg)
    print ("Exiting...")
    exit()

def check_synergies(check_champs, all_syn, all_champs, enable_fates):
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

    fates   = [ "Adept",
                "Assassin",
                "Brawler",
                "Cultist",
                "Divine",
                "Duelist",
                "Dragonsoul",
                "Elderwood",
                "Enlightened",
                "Executioner"
                "Fabled",
                "Fortune",
                "Keeper",
                "Mage",
                "Mystic",
                "Sharpshooter",
                "Slayer",
                "Spirit",
                "Syphoner",
                "Warlord",
                "Vanguard"]

    synergy_tally = {}
    synergy_set   = []
    for cur_trait in traits: synergy_tally[cur_trait] = 0
    for cur_champ in check_champs:
        for cur_trait in all_champs[cur_champ]["Traits"]:
            synergy_tally[cur_trait] += 1
            if cur_trait not in synergy_set: synergy_set.append(cur_trait)
            
    chosen = False
    chosen_fate = None
    for synergy in synergy_set:
        if synergy_tally[synergy] not in all_syn[synergy]:
            # Try to make the trait chosen, since it fails anyway!
            if synergy in fates and not chosen and enable_fates:
                synergy_tally[synergy] += 1
                chosen = True
                chosen_fate = synergy
                if synergy_tally[synergy] not in all_syn[synergy]:
                    return [False, chosen_fate]
            else:
                return [False, chosen_fate]
    return [True, chosen_fate]

# Uses test case for Lee Sin and Jax
def testPass(all_syn, all_champs, enable_fates):
    return check_synergies(["Lee Sin","Jax"], all_syn, all_champs, enable_fates)[0]
    
def testFail(all_syn, all_champs, enable_fates):
    case_1 = check_synergies(["Lee Sin","Xin Zhao","Jax"], all_syn, all_champs, enable_fates)[0]
    case_2 = check_synergies(["Sett"], all_syn, all_champs, enable_fates)[0]
    return (case_1 and case_2)

def run_tests(all_syn, all_champs, enable_fates):
    isPerf = testPass(synergy_data, champion_data, enable_fates)
    if isPerf: print("Perfect synergy test passed!")
    else: print("Perfect synergy test failed...")

    isPerf = testFail(synergy_data, champion_data, enable_fates)
    if isPerf: print("Imperfect synergy test passed!")
    else: print("Imperfect synergy test failed...")

#########################
# Main code begins here #
#########################

parser = ArgumentParser(description='A program to find perfect synergies in TFT.')
parser.add_argument('--max_cost',type=int, help='Max cost to calculate up to. Max 9 and default 7.')
parser.add_argument('--min_cost',type=int, help='Min cost to start from. Min 1 and default 1.')
parser.add_argument('-f','--fates',action='store_true', help='Add to enable fates. Default is disabled.')
args = parser.parse_args()

max_cost = args.max_cost if args.max_cost else 7
min_cost = args.min_cost if args.min_cost else 1
if min_cost >= max_cost: _exit("Minimum cost provided is too low.")
enable_fates = args.fates if args.fates else False


champion_data = None
with open("../Data/Champions.yaml", 'r') as stream:
    champion_data = safe_load(stream)
if champion_data is None: _exit("Champion data not loaded properly.")

champ_list = list(champion_data.keys())
synergy_data = None
with open("../Data/Synergies.yaml", 'r') as stream:
    synergy_data = safe_load(stream)
if synergy_data is None: _exit("Synergy data not loaded properly.")


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
    while i<=costs_at_level[str(level)]:
        champs_by_level[str(level)] += champs_by_cost[str(i)]
        i+=1

total_perf = 0
for level in range(min_cost,(max_cost+1),1):
    print ("Running on level: ",str(level))
    test_list = combinations(champs_by_level[str(level)], level)
    print ("List made")
    perfect_syn = []
    for cur_syn in test_list:
        results = check_synergies(cur_syn, synergy_data, champion_data, enable_fates)
        if results[0]:
            cur_syn = list(cur_syn)
            cur_syn.append("Fate: "+str(results[1]))
            perfect_syn.append(cur_syn)

    print (str(len(perfect_syn)) + " found!")
    print (perfect_syn)
    total_perf += len(perfect_syn)
    oname = ''.join(["Perfect_level",str(level),".yaml"])
    if enable_fates:
        oname = ''.join(["Perfect_level",str(level),"_wFates",".yaml"])

    with io.open(oname, 'w', encoding='utf8') as out_file:
        dump(perfect_syn, out_file, default_flow_style=False, allow_unicode=True)


print ("Total perfect synergies: ", total_perf)
print("Done")

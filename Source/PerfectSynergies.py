#########################################################
# Find the perfect Synergies for a team of two or more! #
#########################################################
import io
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
isSolved = {"One":True, "Two":True,
            "Three":True, "Four":True,
            "Five":True, "Six":True,
            "Seven":True, "Eight":True,
            "Nine": False}
champion_data = None
with open("../Data/Champions.yaml", 'r') as stream:
    champion_data = safe_load(stream)
champ_list = list(champion_data.keys())
print (champ_list)
synergy_data = None
with open("../Data/Synergies.yaml", 'r') as stream:
    synergy_data = safe_load(stream)

# Run test to make sure simple cases are working
run_tests(synergy_data, champion_data)

# Run combination code
total_perf = 0
# 1 man team
print ("* Perfect one-champ comp ****************")
nChamps = len(champion_data)
i = 0
team_comp = []
perfect_comps = []
while (i<nChamps and not isSolved["One"]):
    team_comp.append(champ_list[i])
    
    if checkSynergies(team_comp, synergy_data, champion_data):
        perfect_comps.append(team_comp)
    team_comp = []
    i+=1
if perfect_comps == []:
    print ("No perfect comps")
else: 
    print (str(len(perfect_comps)) + " found!")
    print (perfect_comps)
    total_perf += len(perfect_comps)
    with io.open('Perfect_onecost.yaml', 'w', encoding='utf8') as outfile:
        dump(perfect_comps, outfile, default_flow_style=False, allow_unicode=True)


# 2 man team
print ("* Perfect two-champ comp ****************")
i = 0
team_comp = []
perfect_comps = []
while (i<(nChamps-1) and not isSolved["Two"]):
    # I think a player can get a 2 or 3-star in an orb, so include them
    if champion_data[champ_list[i]]["Cost"] >=4: 
        i+=1
        continue
    j = i+1
    while (j<nChamps):
        if champion_data[champ_list[j]]["Cost"] >=4:
            j+=1
            continue
        team_comp.append(champ_list[i])
        team_comp.append(champ_list[j])
        j+=1
        if checkSynergies(team_comp, synergy_data, champion_data):
            perfect_comps.append(team_comp)
        team_comp = []
    i+=1
if perfect_comps == []:
    print ("No perfect comps")
else: 
    print (str(len(perfect_comps)) + " found!")
    print (perfect_comps)
    total_perf += len(perfect_comps)
    with io.open('Perfect_twocost.yaml', 'w', encoding='utf8') as outfile:
        dump(perfect_comps, outfile, default_flow_style=False, allow_unicode=True)

# 3 man team
print ("* Perfect three-champ comp **************")
i = 0
team_comp = []
perfect_comps = []
while (i<(nChamps-2) and not isSolved["Three"]):
    if champion_data[champ_list[i]]["Cost"] >=4: 
        i+=1
        continue
    j = i+1
    while (j<nChamps-1):
        if champion_data[champ_list[j]]["Cost"] >=4: 
            j+=1
            continue
        k = j+1
        while (k<nChamps): 
            if champion_data[champ_list[k]]["Cost"] >=4: 
                k+=1
                continue
            team_comp.append(champ_list[i])
            team_comp.append(champ_list[j])
            team_comp.append(champ_list[k])
            if checkSynergies(team_comp, synergy_data, champion_data):
                perfect_comps.append(team_comp)
            team_comp = []
            k+=1
        j+=1
    i+=1
if perfect_comps == []:
    print ("No perfect comps")
else: 
     print (str(len(perfect_comps)) + " found!") 
     print (perfect_comps)
     total_perf += len(perfect_comps)
     with io.open('Perfect_threecost.yaml', 'w', encoding='utf8') as outfile:
        dump(perfect_comps, outfile, default_flow_style=False, allow_unicode=True)

# 4 man team
print ("* Perfect four-champ comp ***************")
i = 0
team_comp = []
perfect_comps = []
while (i<(nChamps-3) and not isSolved["Four"]):
    if champion_data[champ_list[i]]["Cost"] >=4: 
        i+=1
        continue
    j = i+1
    while (j<nChamps-2):
        if champion_data[champ_list[j]]["Cost"] >=4: 
            j+=1
            continue
        k = j+1
        while (k<nChamps-1):
            if champion_data[champ_list[k]]["Cost"] >=4: 
                k+=1
                continue
            l=k+1
            while (l<nChamps): 
                if champion_data[champ_list[l]]["Cost"] >=4: 
                    l+=1
                    continue
                team_comp.append(champ_list[i])
                team_comp.append(champ_list[j])
                team_comp.append(champ_list[k])
                team_comp.append(champ_list[l])
                if checkSynergies(team_comp, synergy_data, champion_data):
                    perfect_comps.append(team_comp)
                team_comp = []
                l+=1
            k+=1
        j+=1
    i+=1
if perfect_comps == []:
    print ("No perfect comps")
else: 
    print (str(len(perfect_comps)) + " found!")
    print (perfect_comps)
    total_perf += len(perfect_comps)
    with io.open('Perfect_fourcost.yaml', 'w', encoding='utf8') as outfile:
        dump(perfect_comps, outfile, default_flow_style=False, allow_unicode=True)

# 5 man team
print ("* Perfect five-champ comp ***************")
i = 0
team_comp = []
perfect_comps = []
while (i<(nChamps-4) and not isSolved["Five"]):
    if champion_data[champ_list[i]]["Cost"] >=5: 
        i+=1
        continue
    j = i+1
    while (j<nChamps-3):
        if champion_data[champ_list[j]]["Cost"] >=5: 
            j+=1
            continue
        k = j+1
        while (k<nChamps-2):
            if champion_data[champ_list[k]]["Cost"] >=5: 
                k+=1
                continue 
            l=k+1
            while (l<nChamps-1):
                if champion_data[champ_list[l]]["Cost"] >=5: 
                    l+=1
                    continue 
                m=l+1
                while (m<nChamps):
                    if champion_data[champ_list[m]]["Cost"] >=5: 
                        m+=1
                        continue
                    team_comp.append(champ_list[i])
                    team_comp.append(champ_list[j])
                    team_comp.append(champ_list[k])
                    team_comp.append(champ_list[l])
                    team_comp.append(champ_list[m])
                    if checkSynergies(team_comp, synergy_data, champion_data):
                        perfect_comps.append(team_comp)
                    team_comp = []
                    m+=1
                l+=1
            k+=1
        j+=1
    i+=1
if perfect_comps == []:
    print ("No perfect comps")
else: 
    print (str(len(perfect_comps)) + " found!")
    print (perfect_comps)
    total_perf += len(perfect_comps)
    with io.open('Perfect_fivecost.yaml', 'w', encoding='utf8') as outfile:
        dump(perfect_comps, outfile, default_flow_style=False, allow_unicode=True)

# 6 man team
print ("* Perfect six-champ comp ***************")
i = 0
team_comp = []
perfect_comps = []
while (i<(nChamps-5) and not isSolved["Six"]):
    if champion_data[champ_list[i]]["Cost"] >=5: 
        i+=1
        continue
    j = i+1
    while (j<nChamps-4):
        if champion_data[champ_list[j]]["Cost"] >=5: 
            j+=1
            continue
        k = j+1
        while (k<nChamps-3):
            if champion_data[champ_list[k]]["Cost"] >=5: 
                k+=1
                continue 
            l=k+1
            while (l<nChamps-2):
                if champion_data[champ_list[l]]["Cost"] >=5: 
                    l+=1
                    continue 
                m=l+1
                while (m<nChamps-1):
                    if champion_data[champ_list[m]]["Cost"] >=5: 
                        m+=1
                        continue
                    n=m+1
                    while (n<nChamps):
                        if champion_data[champ_list[n]]["Cost"] >=5: 
                            n+=1
                            continue
                        team_comp.append(champ_list[i])
                        team_comp.append(champ_list[j])
                        team_comp.append(champ_list[k])
                        team_comp.append(champ_list[l])
                        team_comp.append(champ_list[m])
                        team_comp.append(champ_list[n])
                        if checkSynergies(team_comp, synergy_data, champion_data):
                            perfect_comps.append(team_comp)
                        team_comp = []
                        n+=1
                    m+=1
                l+=1
            k+=1
        j+=1
    i+=1
if perfect_comps == []:
    print ("No perfect comps")
else: 
    print (str(len(perfect_comps)) + " found!")
    print (perfect_comps)
    total_perf += len(perfect_comps)
    with io.open('Perfect_sixcost.yaml', 'w', encoding='utf8') as outfile:
        dump(perfect_comps, outfile, default_flow_style=False, allow_unicode=True)


# 7 man team
print ("* Perfect seven-champ comp ***************")
i = 0
team_comp = []
perfect_comps = []
while (i<(nChamps-6) and not isSolved["Seven"]):
    if champion_data[champ_list[i]]["Cost"] >=999: 
        i+=1
        continue
    j = i+1
    while (j<nChamps-5):
        if champion_data[champ_list[j]]["Cost"] >=999: 
            j+=1
            continue
        k = j+1
        while (k<nChamps-4):
            if champion_data[champ_list[k]]["Cost"] >=999: 
                k+=1
                continue 
            l=k+1
            while (l<nChamps-3):
                if champion_data[champ_list[l]]["Cost"] >=999: 
                    l+=1
                    continue 
                m=l+1
                while (m<nChamps-2):
                    if champion_data[champ_list[m]]["Cost"] >=999: 
                        m+=1
                        continue
                    n=m+1
                    while (n<nChamps-1):
                        if champion_data[champ_list[n]]["Cost"] >=999: 
                            n+=1
                            continue
                        p=n+1
                        while (p<nChamps):
                            if champion_data[champ_list[p]]["Cost"] >=999: 
                                p+=1
                                continue
                            team_comp.append(champ_list[i])
                            team_comp.append(champ_list[j])
                            team_comp.append(champ_list[k])
                            team_comp.append(champ_list[l])
                            team_comp.append(champ_list[m])
                            team_comp.append(champ_list[n])
                            team_comp.append(champ_list[p])
                            if checkSynergies(team_comp, synergy_data, champion_data):
                                print ("Perfect comp found!")
                                perfect_comps.append(team_comp)
                            team_comp = []
                            p+=1
                        n+=1
                    m+=1
                l+=1
            k+=1
        j+=1
    i+=1
if perfect_comps == []:
    print ("No perfect comps")
else: 
    print (str(len(perfect_comps)) + " found!")
    print (perfect_comps)
    total_perf += len(perfect_comps)
    with io.open('Perfect_sevencost.yaml', 'w', encoding='utf8') as outfile:
        dump(perfect_comps, outfile, default_flow_style=False, allow_unicode=True)


# 8 man team
print ("* Perfect eight-champ comp ***************")
i = 0
team_comp = []
perfect_comps = []
print (champion_data)
while (i<(nChamps-7) and not isSolved["Eight"]):
    if champion_data[champ_list[i]]["Cost"] >=999: 
        i+=1
        continue
    j = i+1
    while (j<nChamps-6):
        if champion_data[champ_list[j]]["Cost"] >=999: 
            j+=1
            continue
        k = j+1
        while (k<nChamps-5):
            if champion_data[champ_list[k]]["Cost"] >=999: 
                k+=1
                continue 
            l=k+1
            while (l<nChamps-4):
                if champion_data[champ_list[l]]["Cost"] >=999: 
                    l+=1
                    continue 
                m=l+1
                while (m<nChamps-3):
                    if champion_data[champ_list[m]]["Cost"] >=999: 
                        m+=1
                        continue
                    n=m+1
                    while (n<nChamps-2):
                        if champion_data[champ_list[n]]["Cost"] >=999: 
                            n+=1
                            continue
                        p=n+1
                        while (p<nChamps-1):
                            if champion_data[champ_list[p]]["Cost"] >=999: 
                                p+=1
                                continue
                            q=p+1
                            while (q<nChamps):
                                if champion_data[champ_list[q]]["Cost"] >=999: 
                                    q+=1
                                    continue
                                team_comp.append(champ_list[i])
                                team_comp.append(champ_list[j])
                                team_comp.append(champ_list[k])
                                team_comp.append(champ_list[l])
                                team_comp.append(champ_list[m])
                                team_comp.append(champ_list[n])
                                team_comp.append(champ_list[p])
                                team_comp.append(champ_list[q])
                                if checkSynergies(team_comp, synergy_data, champion_data):
                                    print ("Perfect comp found!")
                                    perfect_comps.append(team_comp)
                                team_comp = []
                                q+=1
                            p+=1
                        n+=1
                    m+=1
                l+=1
            k+=1
        j+=1
    i+=1
if perfect_comps == []:
    print ("No perfect comps")
else: 
    print (str(len(perfect_comps)) + " found!")
    print (perfect_comps)
    total_perf += len(perfect_comps)
    with io.open('Perfect_eightcost.yaml', 'w', encoding='utf8') as outfile:
        dump(perfect_comps, outfile, default_flow_style=False, allow_unicode=True)


# 9 man team
print ("* Perfect nine-champ comp *****************")
i = 0
team_comp = []
perfect_comps = []
while (i<(nChamps-8) and not isSolved["Nine"]):
    if champion_data[champ_list[i]]["Cost"] >=999: 
        i+=1
        continue
    j = i+1
    while (j<nChamps-7):
        if champion_data[champ_list[j]]["Cost"] >=999: 
            j+=1
            continue
        k = j+1
        while (k<nChamps-6):
            if champion_data[champ_list[k]]["Cost"] >=999: 
                k+=1
                continue 
            l=k+1
            while (l<nChamps-5):
                if champion_data[champ_list[l]]["Cost"] >=999: 
                    l+=1
                    continue 
                m=l+1
                while (m<nChamps-4):
                    if champion_data[champ_list[m]]["Cost"] >=999: 
                        m+=1
                        continue
                    n=m+1
                    while (n<nChamps-3):
                        if champion_data[champ_list[n]]["Cost"] >=999: 
                            n+=1
                            continue
                        p=n+1
                        while (p<nChamps-2):
                            if champion_data[champ_list[p]]["Cost"] >=999: 
                                p+=1
                                continue
                            q=p+1
                            while (q<nChamps-1):
                                if champion_data[champ_list[q]]["Cost"] >=999: 
                                    q+=1
                                    continue
                                r=q+1
                                while (r<nChamps):
                                    if champion_data[champ_list[r]]["Cost"] >=999: 
                                        r+=1
                                        continue
                                    team_comp.append(champ_list[i])
                                    team_comp.append(champ_list[j])
                                    team_comp.append(champ_list[k])
                                    team_comp.append(champ_list[l])
                                    team_comp.append(champ_list[m])
                                    team_comp.append(champ_list[n])
                                    team_comp.append(champ_list[p])
                                    team_comp.append(champ_list[q])
                                    team_comp.append(champ_list[r])
                                    if checkSynergies(team_comp, synergy_data, champion_data):
                                        print ("Perfect comp found!")
                                        perfect_comps.append(team_comp)
                                    team_comp = []
                                    r+=1
                                q+=1
                            p+=1
                        n+=1
                    m+=1
                l+=1
            k+=1
        j+=1
    i+=1
if perfect_comps == []:
    print ("No perfect comps")
else: 
    print (str(len(perfect_comps)) + " found!")
    print (perfect_comps)
    total_perf += len(perfect_comps)
    with io.open('Perfect_ninecost.yaml', 'w', encoding='utf8') as outfile:
        dump(perfect_comps, outfile, default_flow_style=False, allow_unicode=True)









print ("The total number of perfect team comps is: " + str(total_perf))
print ("Done.")

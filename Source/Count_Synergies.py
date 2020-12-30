##############################################
# Count the total synergies for the known PS #
##############################################

from yaml import safe_load, dump

cost_text = {"2":"twocost",
             "4":"fourcost",
             "5":"fivecost",
             "6":"sixcost",
             "7":"sevencost",
             "8":"eightcost"} # No ninecost in this yet!
for cost, ct in cost_text.items():
    #ct = cost_text[str(cost)]
    with open(''.join(["../Output/Perfect_",ct,".yaml"]), 'r') as stream:
        data = safe_load(stream)
        print (len(data))


from yaml import safe_load, dump

champion_data = None
with open("../Data/Champions.yaml", 'r') as stream:
    champion_data = safe_load(stream)

print( champion_data )



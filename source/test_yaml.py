'''
Simple function to printout the champions from the yaml.
Helpful for data entry debugging.
'''
from yaml import safe_load

CHAMPION_DATA = None
with open("../data/Champions.yaml", 'r') as stream:
    CHAMPION_DATA = safe_load(stream)
print( CHAMPION_DATA )

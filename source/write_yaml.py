'''
Simple function to writeout some example champions
to a yaml file.
Useful for data entry tests.
'''
import io
from yaml import dump

champions = {}
champions["Ahri"] = {}
champions["Ahri"]["cost"] = 2
champions["Ahri"]["Traits"] = ["Sorcerer", "Star Guardian"]

champions["Annie"] = {}
champions["Annie"]["cost"] = 2
champions["Annie"]["Traits"] = ["Sorcerer", "Mech Pilot"]

with io.open('data.yaml', 'w', encoding='utf8') as outfile:
    dump(champions, outfile, default_flow_style=False, allow_unicode=True)
print("Done")

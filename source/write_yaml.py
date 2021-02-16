from yaml import safe_load, dump
import io

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


# TFTAna
All code and results in this git was designed and created by DAbbott
## Description
This code originates from the desire to find every combination of a "Perfect Synergy".
Perfect Synergies are when every champion trait is perfectly utilized.
This code was originally made to run on set 3.5+, which has a level 9 cap with exception to FON.
FON comps are not considered at the moment. This greatly complicates the perfect synergies as
it allows X+1 comps to be accessed for level X, while still have level X type probabilities.
## Examples
An example level-four perfect synergy is Blitzcrank, Ezreal, Illaoi, Kog Maw,
which uses 2/2 Chrono, 2/2 Battlecast, 2/2 Brawler, and 2/2 Blaster.
An example imperfect synergy is Ahri, Syndra, Zoe, which uses 3/3 Star
Guardians and 3/2 Sorcerers.
## Performance
This code uses python3 and has not been tested with any other version of python.
This code has not been optimized and uses a brute-force method to find perfect synergies.
Thus, the code is robust but factorally more complicated for each level/champion added.
Unoptimized level 9 perfect synergies may take days to find with the unopitmized code on a single core.
## How to Run
`python Source/PerfectSynergies.py # Finds the perfect synergies and prints to a .yaml`
`python Source/AnalyzeSynergies.py # Analyses the Output/*.yaml `

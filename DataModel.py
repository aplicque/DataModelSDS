# this is JSON written in python
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
# https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

import json

data = {'metadata': [], 'solubility': []}

data['metadata'].append({
    ' Reference ': ' https://doi.org/10.1021/je60077a008 ',
    ' Title ': ' Solubility and diffusivity of gases in aqueous solutions of amines ',
    ' Component_1': ' Ethylene ',
    ' Component_2': ' 1-Amino-2-Propanol ',
    ' Component_3': ' Water '
})


data['solubility'].append({
    ' Temperature ': 298.15,
    ' Temperature_Unit': ' K ',
    ' Pressure ': 101.3,
    ' Pressure_Unit ': ' kPa '
})

with open('SDSDataModel.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

# indent=4 makes it print nicely and not on one line
# running the code makes the json file in the documents folder


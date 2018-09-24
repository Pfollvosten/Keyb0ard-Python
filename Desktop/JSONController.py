# JSONController.py

import json

data = {}
data['btnmap'] = []

for i in range(8):
    data['btnmap'].append({
        'key_comb' : [],
        'blinkstick' : {},
        'yeelight' : {}
    })

with open('btnmap.json', 'w') as outfile:  
    json.dump(data, outfile, indent=4)
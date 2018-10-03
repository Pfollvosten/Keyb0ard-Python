import json

file =  open('btnmap.json', encoding='utf-8')
data = json.load(file)

HOST = data["settings"]["HOST"]
PORT = data["btnmap"]["PORT"]
B_TIME = data["btnmap"]["b-time"]
POLL_RATE = data["btnmap"]["polling-rate"]
        
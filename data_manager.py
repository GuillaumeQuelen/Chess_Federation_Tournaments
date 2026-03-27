import os
import json

def save_players(players):
    os.makedirs("data", exist_ok=True)
    with open("data/players.json", "w") as f:
        json.dump([p.to_dict() for p in players], f, indent=4)

def load_players():
    if os.path.exists("data/players.json"):
        with open("data/players.json", "r") as f:
            return json.load(f)
    return []
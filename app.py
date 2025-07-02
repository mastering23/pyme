import yaml
import requests
import pandas as pd


with open("application.yaml", "r") as file:
    config = yaml.safe_load(file)

base_url = config["base_url"]
pokemon_list = config["pokemon_list"]

data = []

for name in pokemon_list:
    res = requests.get(f"{base_url}{name}")
    poke = res.json()
    data.append({
        "name": name,
        "base_experience": poke["base_experience"],
        "weight": poke["weight"],
        "type": poke["types"][0]["type"]["name"],
        "ability": poke["abilities"][0]["ability"]["name"]
    })

df = pd.DataFrame(data)
print(df.head())

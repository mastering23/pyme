import yaml
import requests

# Cargar configuración desde application.yaml
with open("application.yaml", "r") as file:
    config = yaml.safe_load(file)

base_url = config["base_url"]
pokemon_list = config["pokemon_list"]

# Recorrer cada Pokémon y mostrar su experiencia base
for name in pokemon_list:
    try:
        response = requests.get(f"{base_url}{name}")
        data = response.json()
        print(f"{name.title()} tiene {data['base_experience']} puntos de experiencia.")
    except Exception as e:
        print(f"Error con {name}: {e}")
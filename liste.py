import json
import requests
from PIL import Image
from io import BytesIO

class Pokemon:
    def __init__(self, name, hp, level, attack, defense, image_url):
        self.name = name
        self.hp = hp
        self.level = level
        self.attack = attack
        self.defense = defense
        self.image_url = image_url

    def to_dict(self):
        return {
            "hp": self.hp,
            "level": self.level,
            "attack": self.attack,
            "defense": self.defense,
            "image_url": self.image_url
        }

    def __str__(self):
        return f"{self.name} (Level: {self.level}) - HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, Image URL: {self.image_url}"

    def show_image(self):
        response = requests.get(self.image_url)
        img = Image.open(BytesIO(response.content))
        img.show()


# Create instances of the Pokemon class with image URLs
charizard = Pokemon("Charizard", 78, 36, 84, 78, "https://pokemondb.net/pokedex/charizard")
blastoise = Pokemon("Blastoise", 79, 36, 83, 100, "https://pokemondb.net/pokedex/blastoise")
venusaur = Pokemon("Venusaur", 80, 36, 82, 83, "https://pokemondb.net/pokedex/venusaur")
pikachu = Pokemon("Pikachu", 35, 25, 55, 40, "https://pokemondb.net/pokedex/pikachu")
jigglypuff = Pokemon("Jigglypuff", 115, 15, 45, 20, "https://pokemondb.net/pokedex/jigglypuff")
gengar = Pokemon("Gengar", 60, 25, 65, 60, "https://pokemondb.net/pokedex/gengar")
gyarados = Pokemon("Gyarados", 95, 40, 125, 79, "https://pokemondb.net/pokedex/gyarados")
lapras = Pokemon("Lapras", 130, 32, 85, 80, "https://pokemondb.net/pokedex/lapras")
ditto = Pokemon("Ditto", 48, 20, 48, 48, "https://pokemondb.net/pokedex/ditto")
eevee = Pokemon("Eevee", 55, 20, 55, 50, "https://pokemondb.net/pokedex/eevee")
vaporeon = Pokemon("Vaporeon", 130, 40, 65, 60, "https://pokemondb.net/pokedex/vaporeon")
jolteon = Pokemon("Jolteon", 65, 40, 65, 60, "https://pokemondb.net/pokedex/jolteon")
flareon = Pokemon("Flareon", 65, 40, 130, 60, "https://pokemondb.net/pokedex/flareon")
snorlax = Pokemon("Snorlax", 160, 35, 110, 65, "https://pokemondb.net/pokedex/snorlax")
articuno = Pokemon("Articuno", 90, 50, 85, 100, "https://pokemondb.net/pokedex/articuno")
zapdos = Pokemon("Zapdos", 90, 50, 90, 85, "https://pokemondb.net/pokedex/zapdos")
moltres = Pokemon("Moltres", 90, 50, 100, 90, "https://pokemondb.net/pokedex/moltres")
dragonite = Pokemon("Dragonite", 91, 55, 134, 95, "https://pokemondb.net/pokedex/dragonite")
mewtwo = Pokemon("Mewtwo", 106, 70, 110, 90, "https://pokemondb.net/pokedex/mewtwo")
mew = Pokemon("Mew", 100, 40, 100, 100, "https://pokemondb.net/pokedex/mew")


# Create a list of Pokemon objects
pokemon_list = [charizard, blastoise, venusaur, pikachu, jigglypuff, gengar, gyarados, lapras, ditto, eevee, vaporeon, jolteon, flareon, snorlax, articuno, zapdos, moltres, dragonite, mewtwo, mew]

# Convert the list of Pokemon objects to a dictionary format
pokemon_data = {pokemon.name: pokemon.to_dict() for pokemon in pokemon_list}

# Save the data to a JSON file
with open("liste.py", "w") as file:
    json.dump(pokemon_data, file, indent=4)

print("Les données des Pokémon ont été sauvegardées dans liste.py")

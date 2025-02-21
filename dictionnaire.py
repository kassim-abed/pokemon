import json

class Type:
    def __init__(self, name, weaknesses, strengths=None):
        self.name = name
        self.weaknesses = weaknesses
        self.strengths = strengths if strengths else []

    def is_weak_to(self, other_type):
        return other_type in self.weaknesses

    def is_strong_against(self, other_type):
        return other_type in self.strengths

    def __str__(self):
        weaknesses = ', '.join(self.weaknesses)
        strengths = ', '.join(self.strengths)
        return f"Type: {self.name}, Weaknesses: {weaknesses}, Strengths: {strengths}"

    def to_dict(self):
        return {
            'name': self.name,
            'weaknesses': self.weaknesses,
            'strengths': self.strengths
        }


# Define all Pokémon types
fire = Type("Fire", weaknesses=["Water", "Rock", "Ground"], strengths=["Grass", "Ice", "Bug", "Steel"])
water = Type("Water", weaknesses=["Electric", "Grass"], strengths=["Fire", "Ground", "Rock"])
grass = Type("Grass", weaknesses=["Fire", "Ice", "Poison", "Flying", "Bug"], strengths=["Water", "Ground", "Rock"])
electric = Type("Electric", weaknesses=["Ground"], strengths=["Water", "Flying"])
ground = Type("Ground", weaknesses=["Water", "Ice", "Grass"], strengths=["Electric", "Fire", "Poison", "Rock", "Steel"])
rock = Type("Rock", weaknesses=["Water", "Grass", "Fighting", "Ground", "Steel"], strengths=["Fire", "Ice", "Flying", "Bug"])
flying = Type("Flying", weaknesses=["Electric", "Ice", "Rock"], strengths=["Grass", "Fighting", "Bug"])
bug = Type("Bug", weaknesses=["Fire", "Flying", "Rock"], strengths=["Grass", "Psychic", "Dark"])
steel = Type("Steel", weaknesses=["Fire", "Fighting", "Ground"], strengths=["Ice", "Rock", "Fairy"])
psychic = Type("Psychic", weaknesses=["Bug", "Ghost", "Dark"], strengths=["Fighting", "Poison"])
ghost = Type("Ghost", weaknesses=["Ghost", "Dark"], strengths=["Psychic", "Ghost"])
dark = Type("Dark", weaknesses=["Fighting", "Bug", "Fairy"], strengths=["Psychic", "Ghost"])
fairy = Type("Fairy", weaknesses=["Poison", "Steel"], strengths=["Fighting", "Dark", "Dragon"])
fighting = Type("Fighting", weaknesses=["Flying", "Psychic", "Fairy"], strengths=["Normal", "Rock", "Ice", "Dark", "Steel"])

class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness

    def display_info(self):
        return f"Superhero Name: {self.name}, Power: {self.power}, Weakness: {self.weakness}"

    def use_power(self):
        return f"{self.name} uses their power: {self.power}!"
class FlyingSuperhero(Superhero):
    def use_power(self):
        return f"{self.name} flies through the sky with their power: {self.power}!"
class TechSuperhero(Superhero):
    def use_power(self):
        return f"{self.name} builds a high-tech gadget using their power: {self.power}!"
hero1 = Superhero("Iron Fist", "Martial Arts Mastery", "Loss of focus")
hero2 = FlyingSuperhero("Falcon", "High-speed flight", "Strong winds")
hero3 = TechSuperhero("Iron Man", "High-tech suits", "Low battery")
print(hero1.display_info())
print(hero2.use_power())
print(hero3.use_power())

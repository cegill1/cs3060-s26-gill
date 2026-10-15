# 3 animal classes: Lion, Giraffe, Monkey
# Food is stored in a FoodDispenser (helper class that helps feed the animals)
# Base class of Animal
    # Attr: name, species
    # Functions: food()
# FoodDispenser Class
    # Class that takes a list of food items (["meat", "banana", "grass", "fish", "nuts"])
    # Functions: dispense()
        # Randomly picks one food item to feed the animals w/o replacement until it runs out of items.
        # If empty, print "No more food left!"
# Hierarchical inheritance

# Lion overrides eat(food) to print "the Lion tears into the meat"
# "" "Giraffe slowly eats the leaves"
# "" "Monkey..."

# Pick a random animal, dispense random food, feed it to the animal (you must call eat).

import random   # contains methods to randomly pick an element from a list 

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self, food):
        pass

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def eat(self, food):
        print(f"{self.name} the Lion tears into the {food}")

class Giraffe(Animal):
    def __init__(self, name):
        super().__init__(name, "Giraffe")

    def eat(self, food):
        print(f"{self.name} the Giraffe slowly chews the {food}")

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name, "Monkey")

    def eat(self, food):
        print(f"{self.name} the Monkey nibbles and plays with the {food}")

class FoodDispenser:
    def __init__(self, food):
        self.foods = foods[:]

    def dispense(self):
        if not self.food_items:
            raise ValueError("Zoo ran out of food!")
        food = random.choice(self.foods)    # Pick random food
        self.foods.remove(food)
        return food

# Instantiation Code
animals = [Lion("Simba"), Giraffe("Melman"), Monkey("George")]
foods = ["meat", "banana", "grass", "fish", "apples"]


# Calling code (outside all class defs)
while True:
    try:
        food = FoodDispenser.dispense()
        animal = random.choice(animals)
        animal.eat(food)
    except ValueError:
        print("Zoo ran out of food!")
        break
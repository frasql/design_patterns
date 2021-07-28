import json
from xml import etree


""" Factory Method (create an object in single step)"""


class JsonExctractor:
    def __init__(self, filepath) -> None:
        self.data = dict()

        with open(filepath, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parse_data(self):
        return self.data


class XMLExctractor:
    def __init__(self, filepath) -> None:
        self.tree = etree.parse(filepath)
        
    @property
    def parse_data(self):
        return self.tree


# passo gli oggetti e li istanzio in un secondo momento quando necessario
def data_exctraction_factory(filepath):
    if filepath.endswith('json'):
        extractor = JsonExctractor
    elif filepath.endswith('xml'):
        extractor = XMLExctractor
    else:
        raise ValueError(f"Cannot exctract data from {filepath}")
    return extractor(filepath)


# decorator add exception
def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = data_exctraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj
     

""" Abstract Factory """

class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} encounters {obstacle} and {act}'
        print(msg)


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eat it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\n\t--------------- Frog World -------------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


# abstract implementation
class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError as err:
        print(f"Age {age} is invalid. Try again....")
        return (False, age)
    return (True, age)


def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
        game = FrogWorld if age < 18 else None
        environment = GameEnvironment(game(name))
        environment.play()
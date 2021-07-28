
# initialize blanck interface
class Person:
    def __init__(self) -> None:
        self.name = None
        self.date_of_birth = None
        self.position = None

    def __str__(self) -> str:
        return f'{self.name} born on {self.date_of_birth} is an {self.position}'

    
    @staticmethod
    def new():
        return PersonBuilder


class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()

    def build(self):
        return self.person 


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_birth):
        self.person.date_of_birth = date_birth
        return self



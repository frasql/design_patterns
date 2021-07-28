
# initialize blanck interface
class Person:
    def __init__(self) -> None:
        self.street_address = None
        self.postcode = None
        self.city = None
        self.company_name = None
        self.position = None
        self.annul_income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}' + \
               f'Employed at {self.company_name} as a {self.position} earning {self.annul_income}'

        
# builder 
class PersonBuilder:
    def __init__(self, person=Person()) -> None:
        self.person = person


    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)


    def build(self):
        return self.person



class PersonJobBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self
        
    def as_a(self, position):
        self.person.position = position
        return self
        

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self
        

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self
        
    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self
        

    def in_city(self, city):
        self.person.city = city
        return self
        

pb = PersonBuilder()
person = pb.lives.at("22 Low").in_city("london").with_postcode("40131").works.at("Bla").as_a("P").earning("100").build()
print(person)
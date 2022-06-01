
class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def hi(self, other_person):
        return f' hi {other_person.name}, my name {self.name} '

David = person('David', 35)
Erika = person('Erika', 32)

print(David.hi(Erika))


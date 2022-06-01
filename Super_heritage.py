
class person():

    def __init__(self, Name, Age, Place) -> None:
        self.name = Name
        self.age = Age
        self.place = Place

    def description(self):
        print( f'Name: {self.name} Age: {self.age} Place: {self.place}')


class Employee(person):
    def __init__(self, salary, years, employee_name, employee_age, employee_place) -> None:

        super().__init__(employee_name, employee_age, employee_place)
        
        self.salary = salary
        self.years = years

    def description(self):
        super().description()

        print( f'Salary: {self.salary} Years: {self.years}')



# Manuelito = Employee(1500, 15, 'Manuel', 55 ,'Brazil' )
Manuelito = person('Manuel', 55 ,'Brazil' )

Manuelito.description()
print(isinstance(Manuelito, Employee))

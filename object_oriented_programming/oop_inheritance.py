# Inherit, extend, override
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def work(self):
        print(f'{self.name} is working...')

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary) # overriding
        self.level = level
    
    def code(self):
        print(f'{self.name} is coding...')

class Designer(Employee):
    def design(self):
        print(f'{self.name} is desiging...')
    
    def work(self):
        print(f'{self.name} is performing design work...') # overriding

se = SoftwareEngineer('SE', 23, 5000, 'Junior')
d = Designer('D', 24, 6000)
se.work()
d.work()
se.code()
d.design()

# Polymorphism
employees_list = [
    SoftwareEngineer('SE', 23, 5000, 'Junior'),
    Designer('D', 24, 6000),
    SoftwareEngineer('SE2', 32, 15000, 'Senior'),
]

def employee_tasks(employees):
    for employee in employees:
        employee.work()

employee_tasks(employees=employees_list)
# List
se1 = ["Software Engineer", "S", 30, "Senior", 3500000]
d1 = ["Designer", "D", 30, "Lead", 5500000]
def code(obj):
    print(f'{obj[1]} is writing code')
code(se1)
code(d1)

# Class
class SoftwareEngineer():
    # Class attribute
    alias = "AI Enabled"

    def __init__(self, name, age, level, salary):
        # Instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    # Instance method
    def code(self):
        print(f'{self.name} is writing code.')
    
    # Instance method
    def language(self, language):
        print(f'{self.name} is writing code in {language}')
    
    # dunder method (double underscore method)
    def __str__(self):
        return f'name = {self.name} age = {self.age} level = {self.level} salary = {self.salary}'
    
    # dunder method (double underscore method)
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # class method
    @staticmethod
    def salary(age):
        if age > 30:
            return 55000000
        return 35000000

# Instance of the class
se1 = SoftwareEngineer("SE1", 30, "Senior", 3500000)
se2 = SoftwareEngineer("SE2", 30, "Lead", 5500000)
se3 = SoftwareEngineer("SE2", 30, "Lead", 5500000)
print(se1)
print(se1.alias)
print(SoftwareEngineer.alias)
print(se1.name)
# print(SoftwareEngineer.name) # error - cannot access instance attributes by class name
se1.code()
se2.code()
se1.language("Python")
se2.language('C++')
print(se1) # calling dunder method __str__
print(se1 == se2) # calling dunder method __eq__
print(se3 == se2) # calling dunder method __eq__
# print(se1.salary(25)) # throws error
print(SoftwareEngineer.salary(25))
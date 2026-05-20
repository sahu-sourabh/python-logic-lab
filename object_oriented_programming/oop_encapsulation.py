# single underscore (_) means protected & double underscore (__) means private.
class SoftwareEngineer:
    def __init__(self, name):
        self.name = name
        self.__salary = None

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, year_of_experience):
        # check value, enforce constraints
        self.__salary = self.__calculate_salary(year_of_experience)
    
    def __calculate_salary(self, year_of_experience):
            return 1000 * year_of_experience

se = SoftwareEngineer("SE")
se.set_salary(5) # Simple form of Abstraction - seperating WHAT from HOW.
print(se.get_salary()) # Similarly print() function is also a simple form of Abstraction.
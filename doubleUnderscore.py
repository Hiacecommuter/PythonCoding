"""
The double underscore (duner) in Python
"""

# 1. __init__
# It is the python class constructor method. The constructor initialize attributes of class instances.

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

Wei = Student('Wei', 'Distinct')

print(Wei.name + '\n' + Wei.grade)
print('*'*20)

# 2. __str__
# It returns the string which represents the instance
class Uni_student(Student):

    def __init__(self, name, grade, uni):
        super().__init__(name, grade)
        self.uni = uni

    def __str__(self):
        return 'This student is from ' + str(self.uni)

Wei01 = Uni_student('Wei01', 'Distinct', 'UOW')

print(Wei01.name + '\n' + Wei01.grade + '\n' + Wei01.uni)
print(Wei01)
print('*'*20)
"""
The returned content of __str__ must be string type. Otherwise a type error will be risen. 
"""

# 3. __repr__
# It returns the string which represents the instance

# 4. __str__ vs __repr__
# __str__ is human-readable format
# __repr__ is machine-readable format. In other words, it is for reconstruction.

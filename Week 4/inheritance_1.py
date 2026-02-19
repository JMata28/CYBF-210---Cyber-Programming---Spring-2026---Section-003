#Example of inheritance
#Additional explanation: https://www.youtube.com/watch?v=RSl87lqOXDE

class Student:
    tuition = 5000

    def __init__(self, first, last, GPA, fees):
        self.first = first 
        self.last = last
        self.GPA = GPA
        self.fees = fees

    def display_data(self):
        print(f"The student {self.first} {self.last} has a GPA of {self.GPA} and costs of ${self.tuition} in tuition and ${self.fees} in fees.") 

class Freshman(Student):
    # pass
    # If the method below is uncommented, then Python will use it instead of the display_data() method in the Student class when the display_data() method is called from a Freshman object
    def display_data(self):
        print(f"The freshman {self.first} {self.last} has a GPA of {self.GPA} and costs of ${self.tuition} in tuition and ${self.fees} in fees.") 

student_1 = Student("Rachel", "Richardson", 4, 200)
freshman_1 = Freshman("Bryan", "Betancourt", 3.5, 350) #You can create instances of Freshman sending the data of the __init__() method for the Student, since Freshman does not have its own __init__() method
student_1.display_data()
freshman_1.display_data()
print(freshman_1.tuition)

# print(help(Freshman)) #This displays useful info about the child class, like the Method Resolution Order

Freshman.tuition = 4000
student_1.display_data()
freshman_1.display_data()#Notice how the class attribute for the child class was found by Python first. We can see that a class attribute in a child class does not affect the class attribute in a parent class' value


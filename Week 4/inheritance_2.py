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
    tuition = 4000

    def __init__(self, first, last, GPA, fees, completed_orientation):
        super().__init__(first, last, GPA, fees) #will use the __init__() method of the parent class Student
        self.completed_orientation = completed_orientation
    
    def orientation_status(self):
        if (self.completed_orientation == True):
            print(f"Freshman {self.first} {self.last} has completed orientation.")
        else:
            print(f"Freshman {self.first} {self.last} has NOT completed orientation.")

class Senior(Student):
    def __init__(self, first, last, GPA, fees, graduation_honors=None):
        super().__init__(first, last, GPA, fees) #will use the __init__() method of the parent class Student
        if (graduation_honors == None):
            self.graduation_honors = []
        else:
            self.graduation_honors = graduation_honors
    
    def add_honor(self, honor):
        self.graduation_honors.append(honor)
        print(f"You have added the honor: {honor} for {self.first} {self.last}.")
    
    def remove_honor(self, honor):
        if honor in self.graduation_honors:
            self.graduation_honors.remove(honor)
        else:
            print(f"Senior {self.first} {self.last} did not have the {honor} honor already.")
    
    def display_honors(self):
        print(f"Senior {self.first} {self.last} has the following graduation honors: ")
        for honor in self.graduation_honors:
            print(honor)

#Test the methods of the sub classes
freshman_1 = Freshman("Bryan", "Betancourt", 3.5, 350, False) 
# freshman_1.orientation_status()

senior_1 = Senior("Phillip", "Pratt", 3.9, 400, ["Dean's List", "Summa Cum Laude"])
# senior_1.display_honors()

senior_2 = Senior("David", "Dennison", 3.2, 400)
# senior_2.add_honor("Student Athlete")
# senior_2.display_honors()
# senior_2.remove_honor("Dean's List")
# senior_2.display_honors()

#isinstance and issubclass
# print(isinstance(freshman_1, Freshman))
# print(isinstance(freshman_1, Student))
# print(isinstance(freshman_1, Senior))

print(issubclass(Freshman, Student))
print(issubclass(Freshman, Senior))
print(issubclass(Student, Freshman))
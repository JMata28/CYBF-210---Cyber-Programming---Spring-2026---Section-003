#The code below helps demonstrate the difference between class attributes and instance attributes
#Source and additional explanation: https://www.youtube.com/watch?v=BJ-VvGyQxho

class Student:
    tuition = 5000 #This is a class attribute. It is the same for all instances of the class objects UNLESS specifically modified for an instance, in which case an instance attribute is created for that instance.

    def __init__(self, first, last, fees):
        self.first = first #This is an instance attribute and it can differ by instance of the object
        self.last = last
        self.fees = fees

    def display_data(self):
        print(f"The student {self.first} {self.last} has costs of {self.tuition} and {self.fees}.") 

student_1 = Student("Rachel", "Richardson", 200)
student_2 = Student("Bryan", "Betancourt", 350)

print(Student.tuition) #Python found the class attribute "tuition", so that's what this line prints.
print(student_1.tuition) #Python did not find an instance attribute "tuition", so it printed the class attribute "tuition" that it found instead
print(student_1.__dict__) #This line displays the instance attributes

student_1.tuition = 4000 #Now that the value of the class attribute has been manually changed, "tuition" now functions as an instance attribute for the student_1 instance
print(student_1.tuition)
print(student_1.__dict__)  #This line displays the instance attributes

# For student_1 below, notice how the .display_data() method still prints 5000 instead of 4000. This is because it is printing the class attribute, not the instance attribute. If the .display_data() method printed self.tuition instead of Student.tuition, then it would print instance attributes
student_1.display_data() 
student_2. display_data()

#Class variables can also be changed, as shown below
Student.tuition = 10000
student_3 = Student("David", "Dennison", 500)
student_3.display_data()
student_2.display_data()
student_1.display_data() #Note how student 1 still displays the instance attribute evene after there was an update to the class attribute

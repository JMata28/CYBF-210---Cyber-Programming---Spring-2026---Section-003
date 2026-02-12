#Example of two common classmethod uses
#Source and additional explanation: https://www.youtube.com/watch?v=rq8cL2XMM5M
class Student:
    tuition = 5000 #This is a class attribute. 

    def __init__(self, first, last):
        self.first = first #This is an instance attribute and it can differ by instance of the object
        self.last = last
    
    @classmethod
    def set_tuition(cls, new_tuition):
        cls.tuition = new_tuition
    
    @classmethod
    def from_string(cls, names):
        first, last = names.split(" ")
        return cls(first, last)

student_1 = Student("Rachel", "Richardson")
print(student_1.tuition)

Student.set_tuition(6000) #changes the class attribute (not the instance attribute)
# # Same thing as Student.tuition = 6000
print(student_1.tuition)

student_2 = Student.from_string("Bryan Betancourt") #instance of class created using a class method as an alternative constructor
print(student_2.first)
print(student_2.last)

#Example of when you want to use a class attribute: counting the instances of a class
#Source and additional explanation: https://www.youtube.com/watch?v=BJ-VvGyQxho
class Student:
    count = 0

    tuition = 5000 #This is a class attribute. It is the same for all instances of the class objects UNLESS specifically modified for an instance, in which case an instance attribute is created for that instance.

    def __init__(self, first, last):
        self.first = first #This is an instance attribute and it can differ by instance of the object
        self.last = last
        Student.count += 1 #Every time the object is created, the class attribute count is increased by 1

print(Student.count) #before any Student object is created

student_1 = Student("Rachel", "Richardson")
print(Student.count)
student_2 = Student("Bryan", "Betancourt")
student_3 = Student("David", "Dennison")
student_4 = Student("Sam", "Simmons")

print(Student.count) #after the Student objects are created
print(student_1.count)
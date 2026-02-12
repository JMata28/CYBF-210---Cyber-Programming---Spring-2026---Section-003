#Example of a staticmethod
#Additional explanation: https://www.youtube.com/watch?v=rq8cL2XMM5M

class Student:

    def __init__(self, first, last):
        self.first = first 
        self.last = last
    
    @staticmethod
    def snow_day(temp): #Notice how the static method does not use information from the Student class or one of its instances
        if temp < 10:
            return True
        return False

student_1 = Student("Rachel", "Richardson")
day_off = Student.snow_day(32)
if(day_off == True):
    print("We have the day off!")
else:
    print("We do have class!")
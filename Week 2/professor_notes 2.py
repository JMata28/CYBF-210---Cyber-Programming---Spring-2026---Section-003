# Uncomment each chunk of code below to run it and remind yourself of the concepts taught in class

#If, else, elif statements:
# home_team = 28
# visiting_team = 24
# if (home_team > visiting_team): #First comparison
#     print("Home team wins!")
# elif(visiting_team > home_team): #Second comparison, will only happen if first comparison returns False
#     print("Visiting team wins!")
# else:
#     print("It's a draw!")   #Default case that happens if neither first and second comparisons return True

#If-else-elif statements within other if-else-elif statements:
#The following code helps us identify which of these animals we are talking about, using if, else, and elif statements to eliminate animals:
# cat, dog, manatee, dolphin, goldfish, and frog
#Lets do this by reviewing lists and using the .remove() list method
# animal_group = "mammal"
# has_fur = True
# feline = False
# herbivore = False
# if (animal_group == "mammal"):
#     if (has_fur == True):
#         if (feline == True):
#             animal ="cat"
#         else:
#             animal ="dog"
#     elif (herbivore ==True):
#         animal = "manatee"
#     else:
#         animal = "dolphin"
# elif (animal_group == "fish"):
#     animal ="goldfish"
# else:
#     animal ="frog"
# print("The animal is: ", animal)

# For loops
# Simple for loop
# fruit_list = ["oranges", "apples", "strawberries", "blueberries"]
# for fruit in fruit_list:  # for and in are keywords. You can use any word instead of fruit as long as you use the same word inside the for loop to refer to the item in the list.
#     print("I like ", fruit)
# For Loop within a For loop
# vegetable_list = ["broccoli", "carrot", "celery"]
# groceries = [fruit_list, vegetable_list]
# for list in groceries:
#     for item in list:
#         print("I like ", item)
#print(groceries[1][:2]) #to access specific item 
# for list in groceries: #to access specific items
#     print(list[:2])
# For loop using range function
# for y in range(3):  # range(3) starts at 0 and goes to 2 in steps of 1 (0,1,2)
#     print(y)
#     print("You should buy: ", fruit_list[y])

# Break in For loop
# for vegetable in vegetable_list:
#     print(vegetable)
#     if (vegetable == "carrot"):
#         break

#While loops
# x = 0
# while x < 6:
#   print(x)
#   x += 1
#   if (x == 4):
#     break

# Functions
#Function with no parameters that doesn't return data
# def message_printing(): #This line defines the function. Notice no parameter is defined, so no data is supposed to be passed into the function
#     print("Hi there!")

# for _ in range (3): #in this case, we don't care about the value of _ That's why we name the variable as an underscore. That's the convention in Python whenever you have a variable whose value you don't care about
#     message_printing() #This line calls the function.
# # Function with parameters that returns data
# import math #This is a Python library that we will need to implement the hypotenuse function below. More on imports in a later class.
# def hypotenuse(a, b):
#     c = math.sqrt((a**2)+(b**2))
#     return c

# answer = hypotenuse(3, 4)
# print("The hypotenuse is: ", answer)

#Classes
#The __init__() method
class Student:
    tuition = 5000
    
    def __init__(self, first, last, GPA, address):
        self.first_name = first
        self.last_name = last
        self.GPA_score = GPA
        self.address_of_student = address
    def name(self):
        print(f"The name of this student is: {self.first_name} {self.last_name}. has a GPA of {self.GPA_score} and their address is {self.address_of_student}")


student_1 = Student("John", "Johnson", 3, "Bridgewater, MA")
print(student_1.first_name)

student_2 = Student("Tyler", "Parker", 4, "Boston. MA")
print(student_2.address_of_student)

student_1.name()
student_2.name()


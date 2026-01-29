# Uncomment each chunk of code below to run it and remind yourself of the concepts taught in class

# # Printing statements
# print("Hello World!")
# print("Welcome to CYBF 210 - Cyber Programming!")

# # Comments
# #Comments can be added by using the numeral or hashtag "#" character. Everything after the # symbol in the line will be ignored
# For multi-line comments, use a # character before each line

# Some immutable data types
students_present = 12  # Integer
average_grade = 99.99  # Float
# Remember Python is case sensitive!! False and True must have their first letter capitalized
daytime_class = True  # Boolean
class_code = "CYBF 210"  # String
# notice snake case, which is typical for Python code

# # Arithmetic Operators
# x = 5 + 7 #Addition. But why isn't this line showing up on our terminal?
# print(x) #It needs the print function for that
# print(12 - 44) #Subtraction
# print(4*3) #Multiplication
# print(10/3) #Division
# print(10%3) #Modulus
# print(5**2) #Exponentiation
# print(15//4) #Floor Division

# # User Input
# answer = input("Choose a number from one to ten.")
#print("You chose number: ", answer)
# #print("Adding one to your number gives: ", answer+1) #gives error because "answer" variable is still a string
# answer_int = int(answer)
# print("Adding one to your number gives: ", answer_int+1)

#Common string functions
# To get the length of a string
class_code = "CYBF 210"  
#length_of_string = print(len(class_code) )
# To access specific characters in a string using indexing (Python is zero-indexed)
# What will the following lines print? Run the program to find out
# print(class_code[0])
# print(class_code[5])
# print(class_code[-1])
# print(class_code[len(class_code)-1])
# print(class_code[:3])
# print(class_code[1:2])
# Escape character in strings is the back slash
# \", \\, \n
#print("The title of the Book is \"The Great Gatsby\"")

# # Formatted strings
# class_code = "CYBF 210" 
# formatted_string = f"This class is {class_code}"
# print(formatted_string)

# # Common string methods
my_sentence = "Pizza is my favorite food."
# Method does not change the original value of string
# print(my_sentence.upper())
# print(my_sentence.lower())
# print(my_sentence.title())
# print(my_sentence.strip())
# print(my_sentence.lstrip())
# print(my_sentence.rstrip())
print(my_sentence.find("zza"))
# # #More methods and Python documentation on built-in types here: https://docs.python.org/3/library/stdtypes.html#string-methods
# print(my_sentence.replace("i", "j"))
# print("Pizzas" in my_sentence)

# #Python Lists
# my_list = [] #creates empty list
# my_list.append("pencil")
# my_list.append("pen")
# my_list.insert(1, "eraser")
# print(my_list)
# my_list.remove("pencil")
# print(my_list)
# my_list.append("pen")
# print(my_list.count("pen"))

# # Dictionaries
# my_dictionary = {
#     "Jane" : 25, 
#     "Austin" : 27,
#     "George" : 20
# }
# print("Jane's age is: ", my_dictionary["Jane"])
# print("George's age is: ", my_dictionary.get("George"))
# print(my_dictionary.keys())
# print(my_dictionary.values())
# my_dictionary["Jane"] = 30
# print("Jane's age is: ", my_dictionary["Jane"])

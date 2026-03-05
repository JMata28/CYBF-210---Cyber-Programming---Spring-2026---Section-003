#Sources and additional explanation: 
# https://www.youtube.com/watch?v=NIWwJbo-9_8 
# https://docs.python.org/3/library/exceptions.html 

#Example 1
def example_1():
    try:
        x = 5/0
    except ZeroDivisionError:
        print("Can't divide by zero.")

#example_1()


#Example 2: What if we had more than one error?
def example_2():
    try: 
        y = undeclared_variable #What would happen if we correct this line? Would we still get an Exception?
        x = 5/0
    except Exception:
        print("Some error was found.")

#example_2()

#Example 3: How to use specific Exceptions
#The first exception found is triggered and the rest of the code stops running
#More exceptions can be defined in the Python documentation: https://docs.python.org/3/library/exceptions.html
def example_3():
    try: 
        y = undeclared_variable
        x = 5/0
    except ZeroDivisionError:
        print("Can't divide by zero.")
    except NameError:
        print("Variable not found.")

#example_3()

#Example 4:
#If you don't have an except statement to catch the right exception type, the usual traceback python error will show and the code will stop running
def example_4():
    try:
        x = 5/0
    except NameError:
        print("Variable not found.")

#example_4()

#Example 5:
#Python checks except blocks in order from top to bottom, so in Example 5, the first except statement that matches the error will. be the one executed. It's best practice to leave "Exception" last to deal with specific errors individually.
def example_5():
    try:
        x = 5/0
    except Exception:
        print("Exception printed")
    except ZeroDivisionError:
        print("Specific exception printed.")

# example_5()

#Example 6: You can print the error message thrown by each exception.
def example_6():
    try: 
        x = 5/0
        #See what error messages you get from the lines below
        # y = undeclared_variable 
        # my_dictionary = {}
        # print(my_dictionary["first_key"])
    except Exception as e:
        print(f"This is the error message that Exception gave: {e}.")

example_6()




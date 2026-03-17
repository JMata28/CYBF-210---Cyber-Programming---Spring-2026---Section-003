#Sources and additional explanation: 
# https://www.youtube.com/watch?v=NIWwJbo-9_8 
# https://docs.python.org/3/library/exceptions.html 

#Example 7: the else statement that goes with a try-except block will execute if no exceptions where raised from errors inside the try block.
def example_7():
    try:
        x = 5/1
        #If we uncomment the line below, our except block will be triggered.
        x = 5/0 
    except Exception as e:
        print(f"This is the error message that Exception gave: {e}.")
    else:
        print("No errors were found!")

#example_7()

def example_8():
    try:
        x = 5/0
    except Exception as e:
        print(f"This is the error message that Exception gave: {e}.")
    finally:
        print("This message prints even though there was an exception!")

#example_8()

def example_9():
    try:
        x = undeclared_variable
    except ZeroDivisionError as e:
        print(f"This is the error message that ZeroDivisionError gave: {e}.")
    finally:
        print("This message will NOT print because the exception was not properly handled so we will get a Python traceback error message.")

#example_9()

#Example 10: Raising our own exceptions.
#See what happens if I do raise an exception but it is not caught.
def example_10():
    a = 0
    if a == 0:
        raise Exception
    print("This line of code won't run because the program crashes since an exception was raised.")

#example_10()

#Example 11:Raising our own exceptions but catching them
def example_11():
    try:
        a = 0
        if a == 0:
            raise Exception
        print("This line of code won't run because the exception is raised before this line is reached.")
    except Exception:
        print("I raised my own exception!")


#example_11()
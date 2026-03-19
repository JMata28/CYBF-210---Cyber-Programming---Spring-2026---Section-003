while(True):
    try:
        #Get first number
        a = input("Please enter the first number: ")
        if (a == "q"):
            break
        a = int(a)
        #Get second number
        b = input("Please enter the second number: ")
        if (b == "q"):
            break
        b = int(b)
        #Get operator
        operator = input("Please enter the operator (+, -, *, /): ")
        if (operator == "q"):
            break
        if (b == 0 and operator == "/"):
            raise ZeroDivisionError
        if operator not in ["+", "-", "*", "/"]:
            raise Exception
    except ValueError:
        print("This character cannot be converted to a number.")
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except Exception:
        print("You encountered an error. Please try again.")
    else:
        if operator == "+":
            #addition
            print(f"{a}+{b}={a+b}")
        elif operator == "-":
            #subtraction
            print(f"{a}-{b}={a-b}")
        elif operator == "*":
            #multiplication
            print(f"{a}*{b}={a*b}")
        elif operator == "/":
            #division
            print(f"{a}/{b}={a/b}")
    finally:
        print("Attempt complete.\n")
print("Ending program now.")
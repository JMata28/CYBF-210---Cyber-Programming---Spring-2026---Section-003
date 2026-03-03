#Another example: recursion to calculate the factorial of a positive integer
#Source and additional explanation: https://www.youtube.com/watch?v=ivl5-snqul8

def iterative_factorial(number):
    if (number > 0):
        result = 1
        for i in range(1, number+1): #We add 1 do the number since the range function goes up to BUT NOT INCLUDING the second argument
            result = result * i
        return result
    else:
        return("Enter a positive number for this function to work.")

# print(iterative_factorial(3))

def recursive_factorial(number):
    if (number > 0):
        if number == 1: #Base condition
            return 1
        return number * recursive_factorial(number - 1)
    else:
        return("Enter a positive number for this function to work.")

print(recursive_factorial(4))
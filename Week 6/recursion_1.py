#Example of recursive vs iterative approach
#Source and additional explanation: https://www.youtube.com/watch?v=ivl5-snqul8

#Let's say we want to count from 1 to 10
#The iterative approach that we know:

def iterative(number):
    for i in range(1, number):
        print(f"Counting number {i}")

#iterative(100)

#Notice in the recursive function below how if you uncomment line 17 and comment out line 19, the numbers are counted from 10 to 1. However, if you comment out line 17 and uncomment line 19, the numbers are counted from 1 to 10. This happens because the print statement in line 19 only happens AFTER the recursive function has reached its conclusion (after it has fully executed), so the first time this happens is when the base condition is achieved when number = 0. After number == 0, the call recursive(1 - 1) has concluded and the following statement is "Counting number 1." After this, the call recursive(2 - 1) is concluded and the following statement is "Counting number 2". And so on and so forth. This works like a "stack" of "frames" where the most recent function to be called needs to be concluded before the one before it can be concluded. However, there is a limit to how many "frames" or un-concluded functions can be in the stack at a time, so be mindful of that. 
def recursive(number):
    if number == 0: #This is our base condition. Since we are assuming that "number" starts as a positive number and that it keeps getting reduced by 1 during the recursion, we know that it will eventually reach zero and therefore, we know that the recursion will stop and not loop infinitely. 
        return
    # print(f"Counting number {number}")
    recursive(number - 1)
    print(f"Counting number {number}")

recursive(1000)
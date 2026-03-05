# Today’s problem is calculating the Fibonacci series using recursion. 
# The problem is described here: https://leetcode.com/problems/fibonacci-number/description/ 
# The solution we will go over is an adaptation of LeetCode user Vaishnav’s solution found here: https://leetcode.com/problems/fibonacci-number/solutions/7205782/with-recursion-python-3 


def recursive_fibonacci(index):
    if index <= 1: #base case
        return index
    return recursive_fibonacci(index - 1) + recursive_fibonacci (index - 2)

print(recursive_fibonacci(10))
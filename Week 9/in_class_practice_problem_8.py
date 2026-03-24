def isValid(s):
    pairs = {
        ")":"(",
        "}":"{", 
        "]":"["
    }
    stack = []
    for character in s:
        #if the character is a closing bracket
        if character in pairs:
            if stack and stack[-1] == pairs[character]:
                stack.pop()
            else:
                return False
        #if the character is an open bracket
        else:
            stack.append(character)
    if stack:
        return False
    else: 
        return True
    
test_string_1 = "()" 
test_string_2 = "()[]{}"
test_string_3 = "(]"
test_string_4 = "([])"

print(isValid(test_string_1)) #True
print(isValid(test_string_2)) #True
print(isValid(test_string_3)) #False
print(isValid(test_string_4)) #True
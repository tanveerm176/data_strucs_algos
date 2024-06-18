# Function to check if a string of brackets is valid
def isValid( s: str) -> bool:
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Stack to hold the opening brackets found in the string
    opening_brackets_stack = []

    # Iterate through each character in the string
    for char in s:
        # If the character is not a closing bracket (hence, it's an opening bracket)
        if char not in bracket_mapping.keys():
            # Push the opening bracket onto the stack
            opening_brackets_stack.append(char)
            # Continue to the next iteration of the loop, skipping the remaining code in this iteration
            continue
        
        # If the current character is a closing bracket, check if there is a matching opening bracket on top of the stack
        if opening_brackets_stack and opening_brackets_stack[-1] == bracket_mapping[char]:
            # Pop the matching opening bracket from the stack
            opening_brackets_stack.pop()
        else:
            # If there is no matching opening bracket, or the stack is empty, return False
            return False

    # After processing all characters, check if the stack is empty
    if len(opening_brackets_stack) == 0:
        # If the stack is empty, all brackets are properly matched and nested, return True
        return True
    else:
        # If the stack is not empty, there are unmatched opening brackets, return False
        return False
    
print(isValid("{{([])}}"))
print(isValid("{([])}}"))

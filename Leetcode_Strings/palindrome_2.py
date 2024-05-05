#write a function that takes a string and returns a valid palindrome 
    # valid palindromes are allowed to skip one character


#UMPIRE:
#can string be empty and all whitespace? YES
#is string always alphabetic chars? YES
#is string always lowercase? YES

def isPalindrome(s, left, right, skip_num):
    s = s.strip()

    if skip_num > 1:
        return False
    
    #string can be empty or full of whitespace
    if s == "":
        return True
    
    #func for valid palindrome using two pointers
    while left < right:
        if s[left] == s[right]:
            left = left + 1
            right = right - 1
        
        else:
            skip_num += 1
            #recursive function
            check_left_skip = isPalindrome(s, left+1, right, skip_num)
            check_right_skip = isPalindrome(s, left, right-1, skip_num)
            return check_left_skip or check_right_skip
    
    return True
    

def validPalindrome(s):
    return isPalindrome(s, 0, len(s)-1, 0)

print(validPalindrome("  "))
print(validPalindrome("abca"))
print(validPalindrome("aa"))
print(validPalindrome("acca"))
print(validPalindrome("aa"))

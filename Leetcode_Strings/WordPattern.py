# https://leetcode.com/problems/word-pattern/
# https://guides.codepath.org/compsci/Word-Pattern#4-i-mplement
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

"""
Understand what the interviewer is asking for by using test cases and questions about the problem.

    Established a set (2-3) of test cases to verify their own solution later.
    Established a set (1-2) of edge cases to verify their solution handles complexities.
    Have fully understood the problem and have no clarifying questions.
    Have you verified any Time/Space Constraints for this problem?

    Does every character map to a single word?
        Each character has to map to a single word. Every word has to map to a single character.
    Should the time and space complexity analyses ignore the size of words?
        Since the size (number of entries) of the two hash maps should be the same, it should be O(1). Whenever the number of distinct words goes beyond the number of distinct letters in the pattern, a False value will be returned immediately.

"""


"""
General Idea: Create two dictionaries that maps words to char and char to word
1. For each (character and word) in the lists respectively, check if the mapping of char to word is in the dictionary (and similar for word to char). 
2. If the dictionary doesn’t yet have the mapping, add to it.
3. If at any instance, the mapping doesn’t match, return false. 
4. If after checking every pair, we still match, that means the pattern matches.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # create a list from the string s, splitting on the whitespace
        words = s.split(" ") #['dog', 'cat', 'cat', 'dog']

        # if the length of the word list and the
        # len of the pattern string dont match return False
        if len(pattern) != len(words):
            return False
        
        #create two dictionaries that will house the char and the word
        wordToChar = {} #{'dog': 'a'} "key: value pairs" **DOES NOT ALLOW DUPLCATE KEYS
        charToWord = {} #{'a':'dog'}

        zipped = zip(pattern, words) #('a', 'dog'), ('b', 'cat'), ('b', 'cat'), ('a', 'dog')
        # char, word = list(zipped)[0] #char = 'a', word = 'dog'


        """
        for each character and word in the zipped tuple list
            if the current character exists in the character to word dictionary 
                AND
            if the word value at that charcter key does not equal the current word from the tuple 
            return False

            if the current word exists in the word to character dictionary 
                AND
            if the character value at that word key does not equal the current character from the tuple 
            return False

            otherwise add the character and words to their respective dicts
        
        return True if neither False condition is met

        """    
        for char, word in zipped:

            if char in charToWord and charToWord[char] != word:
                return False
            
            if word in wordToChar and wordToChar[word] != char:
                return False

            wordToChar[word] = char
            charToWord[char] = word
        
        return True

        # print(wordToChar)
        # print(charToWord)


solution = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(solution.wordPattern(pattern, s))

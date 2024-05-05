"""
Different ways to do it:
"""

def short(s, target="o"):
    # Initialize a result array with "infinity" values (here, len(s)) for each character in the input string.
    result = [len(s)] * len(s)

    def helper(position, distance):
        # Avoid further recursion if the current position already has a shorter (or equal) distance recorded.
        if result[position] <= distance:
            return

        # Update the distance for the current position because a shorter path to the target was found.
        result[position] = distance

        # Recursive case: if not at the right end, move to the right (+1 position) and increase distance by 1.
        if position < len(s) - 1:
            helper(position + 1, distance + 1)

        # Recursive case: if not at the left end, move to the left (-1 position) and increase distance by 1.
        if position > 0:
            helper(position - 1, distance + 1)

    # Main loop through each character in the input string.
    for i in range(len(s)):
        # Check if the current character matches the target. If so, initiate recursion from its position.
        if s[i] == target:
            helper(i, 0)

    # Return the result array which now contains the shortest distances to the target character.
    return result


# Example usage:
# Find the shortest distance from each character to 'e' in the string "hello"
print(short("hello", "e"))


"""
def short(s, target="o"):
    # Initialize the result array with "infinity" values for each character.
    # Use a large value (e.g., len(s)) to represent infinity.
    result = [len(s)] * len(s)

    # First pass: from left to right.
    # Find the distance to the nearest target character on the left.
    last_target_pos = -len(s)  # Initialize with a position far enough to the left.
    for i in range(len(s)):
        if s[i] == target:
            last_target_pos = i  # Update last seen position of the target character.
        result[i] = min(result[i], i - last_target_pos)

    # Second pass: from right to left.
    # Find the distance to the nearest target character on the right.
    last_target_pos = 2 * len(s)  # Initialize with a position far enough to the right.
    for i in range(len(s) - 1, -1, -1):
        if s[i] == target:
            last_target_pos = i  # Update last seen position of the target character.
        result[i] = min(result[i], last_target_pos - i)

    return result

# Example usage:
print(short("hello", "e"))
"""
"""
How It Works:

    Initialization: Create a result array filled with "infinity" (here, the length of s), assuming initially that all characters are infinitely far from the target.

    First Pass (Left to Right): Iterate over the string from left to right. If the current character is the target, update last_target_pos to the current index. Calculate the distance from the current position to the most recently found target character on the left and update the result array accordingly.

    Second Pass (Right to Left): Iterate over the string from right to left. This pass ensures that each character's distance to the nearest target character on the right is also considered. Update last_target_pos whenever the target character is found, and calculate the distance similarly, updating the result array with the minimum distance found so far.

Complexity Analysis:

    Time Complexity: The algorithm makes two passes through the string, each taking O(n) time, where n is the length of the string. Thus, the overall time complexity is O(2n), which simplifies to O(n).

    Space Complexity: The space complexity is primarily due to the result array, which requires O(n) space. No additional significant space is used, so the total space complexity remains O(n).

This non-recursive approach is efficient and straightforward, effectively minimizing the distance calculations to two passes through the input string.
"""

"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [n] * n  # Initialize the result array with "infinity" (here, n).
        
        # First pass: left to right
        last_occurrence = -n  # Initialize to a large negative value.
        for i in range(n):
            if s[i] == c:
                last_occurrence = i
            ans[i] = min(ans[i], i - last_occurrence)
        
        # Second pass: right to left
        last_occurrence = 2 * n  # Initialize to a large positive value.
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_occurrence = i
            ans[i] = min(ans[i], last_occurrence - i)
        
        return ans

"""

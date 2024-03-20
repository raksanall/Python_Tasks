# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            s=s[:i]+s[i+1:]
            if s==s[::-1]:
                return True
            else:
                s=s[:]
        return False 

# Example 1:
# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 
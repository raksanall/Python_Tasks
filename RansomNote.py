# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr=[]
        for i in ransomNote:
            if i in magazine:
                arr.append(i)
                index = magazine.index(i)
                magazine=magazine[:index]+magazine[index+1:]
            else:
                return False
        return ''.join(arr)==ransomNote 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
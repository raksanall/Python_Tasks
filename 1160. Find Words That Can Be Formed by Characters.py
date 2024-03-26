# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        letterCounts=[0 for _ in range(26)]
        ans=0
        for c in chars:
            letterCounts[ord(c)-ord('a')]+=1
        
        for word in words:
            copyOfLetterCounts=letterCounts[::]
            isGoodWord=True
            for c in word:
                if copyOfLetterCounts[ord(c)-ord('a')]==0:
                    isGoodWord=False
                    break
                copyOfLetterCounts[ord(c)-ord('a')]-=1
            if isGoodWord:
                ans+=len(word)
        return ans               

        

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
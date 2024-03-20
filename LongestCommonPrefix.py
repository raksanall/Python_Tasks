# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortWord=min(strs,key=len)
        prefix=shortWord
        for word in strs:
            while not word.startswith(prefix):
               prefix=prefix[:-1]
            if not prefix:
                return ""
        return prefix
        
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
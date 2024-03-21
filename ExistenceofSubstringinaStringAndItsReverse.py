# Given a string s, find any substring of length 2 which is also present in the reverse of s.
# Return true if such a substring exists, and false otherwise.

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        check=set()
        for i in range(0,len(s)-1):
            check.add(s[i])
            check.add(s[i+1])
            if ''.join(check) in s and ''.join(check) in s[::-1]:
                return True
            else:
                check.clear()
        return False
                
# Example 1:
# Input: s = "leetcode"
# Output: true
# Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".
# Example 2:
# Input: s = "abcba"
# Output: true
# Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".
# Example 3:
# Input: s = "abcd"
# Output: false
# Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.


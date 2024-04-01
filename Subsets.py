# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

#First way
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst=[]
        for i in range (len(nums)+1):
            ans=list(itertools.combinations(nums,i))
            lst.extend([list(comb)for comb in ans])
        return lst
    
#Second way:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr=[[]]
        for j in nums:
            arr+=[i+[j] for i in arr]
        return arr    
# third way with backtracking:

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def count(start, cur):
            ans.append(cur[:])
            for i in range(start, len(nums)):
                cur.append(nums[i])
                count(i + 1, cur)
                cur.pop()
        count(0, [])
        return ans
    
    
# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
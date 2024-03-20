# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start==len(nums):
                permutations.append(nums[:])
            else:
                for i in range (start,len(nums)):
                    nums[start],nums[i]=nums[i],nums[start]
                    backtrack(start+1)
                    nums[start],nums[i]=nums[i],nums[start]
        permutations=[]
        backtrack(0)
        return permutations

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]

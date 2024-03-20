# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        maxCount=1
        mostRepeated=nums[0]
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
                count+=1
            if count>maxCount:
                maxCount=count
                mostRepeated=nums[i]
            if not nums[i]==nums[i+1]:
                count=1
        return mostRepeated

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
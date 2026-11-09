# Problem: Two Sum (LeetCode #1)
# Link: https://leetcode.com/problems/two-sum/
# Question: Find two numbers in the array whose sum equals the target.
# Approach: Store numbers in a dictionary, one pass.
# Time Complexity: O(n)
# Status: Solved

# first way to solve it by dic ,less time complexity :
# from typing import List

class Solution:
    def twoSum(self, nums, target) :
        seen = {} # TO STORE THE PREVIOUS NUMBER WITH INDEX || NUMBER:INDEX
        for i, n in enumerate(nums):
            # i = 0,1,2,3,..
            # n = 2,7,11,15 ..
            if target - n in seen: # target-n > give us the next number that we want and helps us to find their index
                return [seen[target - n], i]
            seen[n] = i # storing the num:index to see in future

# print(Solution().twoSum([2, 7, 11, 15], 9))

# second way but TC in O(n2)
# indexing like i + i+1 
# [2,11,7,15]
#  0 1  2  3   || 0+1...0+3 then 1+2..1+3 then 2+3 
# class Solution:
#     def twoSum(self, nums, target) :
#         for j in range(len(nums)): # j = 0,1,2,3,
#             for i in range(j+1,len(nums)):  # (i is always j + 1)0+1...0+3 then 1+2..1+3 then 2+3 
#                 if nums[j]+nums[i] == target:
#                     return [j,i]

print(Solution().twoSum([2, 7, 11, 15], 9))
# Problem: Two Sum (LeetCode #1)
# Link: https://leetcode.com/problems/two-sum/
# Question: Find two numbers in the array whose sum equals the target.
# Approach: Store numbers in a dictionary, one pass.
# Time Complexity: O(n)
# Status: Solved

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i

# print(Solution().twoSum([2, 7, 11, 15], 9))
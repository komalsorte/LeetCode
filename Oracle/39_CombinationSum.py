"""
LeetCode - Medium
"""
"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
"""


class Solution:
    def combinationSum(self, nums, target: int):
        n = 0
        combinations = list()
        self.dfs(n, nums, [], combinations, target)
        return combinations

    def dfs(self, index, nums, current_combination, combinations, target):
        current_sum = sum(current_combination)
        if current_sum == target:
            combinations.append(list(current_combination))
        if current_sum < target:

            while index < len(nums):

                current_combination.append(nums[index])
                self.dfs(index, nums, current_combination, combinations, target)
                current_combination.pop()
                index += 1

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().combinationSum(nums, 5))

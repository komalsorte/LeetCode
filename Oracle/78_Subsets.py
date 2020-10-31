"""
LeetCode - Medium
"""
"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:

    def subsets(self, nums):
        n = 0
        combinations = list()
        self.dfs(n, nums, [], combinations)
        return combinations[1:]



    def dfs(self, index, nums, current_combination, combinations):
        combinations.append(list(current_combination))

        while index < len(nums):
            current_combination.append(nums[index])
            self.dfs(index + 1, nums, current_combination, combinations)
            current_combination.pop()
            index += 1




if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    nums = ["b", "a", "c", "a"]
    print(Solution().subsets(nums))

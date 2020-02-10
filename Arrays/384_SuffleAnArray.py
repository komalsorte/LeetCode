"""
LeetCode - Medium
"""
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original_nums = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        org_list = self.original_nums
        self.nums = list(org_list)
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        suffled_list = []
        while len(self.nums) != 0:
            index = random.randint(0, len(self.nums)-1)
            suffled_list.append(self.nums[index])
            self.nums.pop(index)
        self.nums = suffled_list
        return self.nums

# Your Solution object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [-6,10,184]
    obj = Solution(nums)

    for i in range(1000):
        param_2 = obj.shuffle()
        param_1 = obj.reset()
        print(param_2)
        print(param_1)
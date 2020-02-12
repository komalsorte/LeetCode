"""
LeetCode - Easy
"""
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_substring = 0
        s_copy = s
        current_substring = ""
        while len(s_copy) !=0:
            if s_copy[0] == 'R' and current_substring == "":
                current_substring = current_substring + 'R'
            elif s_copy[0] == 'L' and current_substring == "":
                current_substring = current_substring = 'L'



if __name__ == '__main__':
    Solution().balancedStringSplit("RL")

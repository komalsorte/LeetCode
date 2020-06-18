__author__ = 'Komal Atul Sorte'
"""
Given a string, find the length of the longest substring without repeating characters.
"""


class Solution:
    def longestSubstring(self, s):
        if s == " ":
            return 1
        ele_list = list()
        max = 0
        res = ""
        index, start = 0, 0
        while start < len(s) and index < len(s):
            if s[index] in ele_list:
                start += 1
                index = start
                if max < len(res):
                    max = len(res)
                res = ""
                ele_list = list()
            else:
                res = res + s[index]
                ele_list.append(s[index])
                index += 1
        if max < len(res):
            max = len(res)
        return max


if __name__ == '__main__':
    input = "abcabcbb"
    input = "c"
    input = "dvdf"
    print(Solution().longestSubstring(s=input))

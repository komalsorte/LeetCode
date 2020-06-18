__author__ = 'Komal Atul Sorte'
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s):
        count_char = dict()
        if s == "":
            return -1
        for char in s:
            if char in count_char:
                count_char[char] += 1
            else:
                count_char[char] = 1
        print(count_char)

        for i in range(len(s)):
            if count_char[s[i]] == 1:
                return i
        return -1



if __name__ == '__main__':
    input = "leetcode"
    input = "loveleetcode"
    input = "cc"
    print(Solution().firstUniqChar(input))
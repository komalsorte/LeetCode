"""
LeetCode - Easy
"""
"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""

from collections import Counter, OrderedDict

class Solution:
    def firstUniqChar(self, s):
        # count = Counter(s)
        #
        # # find the index
        # for idx, ch in enumerate(s):
        #     if count[ch] == 1:
        #         return idx
        # return -1
        character_tracker = OrderedDict()
        for i, value in enumerate(s):
            character_tracker[value] = character_tracker.get(value, 0) + 1

        for i, value in enumerate(s):
            if character_tracker[value] == 1:
                return i
        return -1

if __name__ == '__main__':
    s = "ccop"
    print(Solution().firstUniqChar(s))
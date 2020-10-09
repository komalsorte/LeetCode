"""
LeetCode - Easy
"""
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""


class Solution:
    def isIsomorphic(self, s, t):
        s_mapper = {}
        t_mapper = {}

        for i in range(len(s)):
            s_mapper[s[i]] = s_mapper.get(s[i], []) + [i]
            t_mapper[t[i]] = t_mapper.get(t[i], []) + [i]

        if sorted(s_mapper.values()) == sorted(t_mapper.values()):
            return True
        else:
            return False


if __name__ == '__main__':
    s = "foo"
    t = "baa"
    print(Solution().isIsomorphic(s, t))

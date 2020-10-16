"""
LeetCode - Easy
"""
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = re.sub('[\W_]+', '', s)
        s = ''.join(s.split())
        s = s.lower()
        print(s)
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    s = "race a car"
    s = "A man, a plan, a canal: Panama"
    s = "ab_a"
    print(Solution().isPalindrome(s))

__author__ = "Komal Atul Sorte"
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    # Passes 101/103 test cases
    def longestPalindrome(self, s):
        if s == "":
            return ""
        start, end, flag = 0, len(s) - 1, False
        longestPaliLen = float('-inf')
        longestPali = None

        while start != len(s):
            if end - start + 1 > longestPaliLen:
                flag = self.longestPalindromeHelper(start, end, s)
                if flag and longestPaliLen < end - start + 1:
                    longestPaliLen = end - start + 1
                    longestPali = [start, end + 1]
                end -= 1
                if start > end:
                    start += 1
                    end = len(s) - 1
            else:
                start += 1
                end = len(s) - 1
        return s[longestPali[0]: longestPali[1]]

    def longestPalindromeHelper(self, start, end, s):
        while start < end:
            if s[start] == s[end]:
                start, end = start + 1, end - 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = "babad"
    # s = ""
    print(Solution().longestPalindrome(s))

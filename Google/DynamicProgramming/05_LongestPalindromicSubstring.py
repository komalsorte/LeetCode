"""
LeetCode - Medium
"""
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

# Not complete
class Solution:

    def longestPalindrome(self, s):
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        indexItr, start, end = 1, 0, 0

        longestPalindromeSubstring = ""
        for i in range(len(s)):
            dp[i][i] = 1
            if len(s[i]) > len(longestPalindromeSubstring):
                longestPalindromeSubstring = s[i]

        while indexItr < len(s):
            if indexItr == 1:
                end = start + 1
                if s[start] == s[end]:
                    dp[start][end] = 1
                    if end - start > len(longestPalindromeSubstring) - 1:
                        longestPalindromeSubstring = s[start: end + 1]
                start += 1
            else:
                end = start + indexItr
                if s[start] == s[end] and dp[start + 1][end - 1] == 1:
                    dp[start][end] = 1
                    if end - start > len(longestPalindromeSubstring) - 1:
                        longestPalindromeSubstring = s[start: end + 1]
                start += 1

            if start + indexItr >= len(s):
                indexItr += 1
                start = 0
                end = indexItr
        print(dp)
        return longestPalindromeSubstring




if __name__ == '__main__':
    s = "aaaabbaa"
    s = "a"
    s = "cbbd"
    print(Solution().longestPalindrome(s))

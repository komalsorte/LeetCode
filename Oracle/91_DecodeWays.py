"""
LeetCode - Medium
"""

"""

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:

Input: s = "1"
Output: 1
 
"""


class Solution:
    def __init__(self):
        self.memo = {}

    def recursive_with_memo(self, index, s) -> int:
        if index == len(s):
            return 1

        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        if index in self.memo:
            return self.memo[index]

        left = self.recursive_with_memo(index + 1, s)
        if int(s[index: index + 2]) <= 26 and int(s[index: index + 2]) >= 10:
            right = self.recursive_with_memo(index + 2, s)
        else:
            right = 0
        self.memo[index] = left + right
        return left + right

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.recursive_with_memo(0, s)


if __name__ == '__main__':
    s = "2316"
    print(Solution().numDecodings(s))

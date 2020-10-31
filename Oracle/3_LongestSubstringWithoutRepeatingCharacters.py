"""
LeetCode - Medium
"""
"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        substring_set, max_length = set(), 0
        while start < len(s):
            if s[end] not in substring_set:
                substring_set.add(s[end])
                end += 1

            if end == len(s) or s[end] in substring_set:
                start += 1
                end = start
                max_length = max(max_length, len(substring_set))
                substring_set = set()

        return max_length

if __name__ == '__main__':
    s = "ababc"
    print(Solution().lengthOfLongestSubstring(s))

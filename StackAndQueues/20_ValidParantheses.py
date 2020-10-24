"""
LeetCode - Easy
"""
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


class Solution:
    def __init__(self):
        self.stack = list()
        self.brackets = {"}": "{", ")": "(", "]": "[", ">": "<"}
        self.opening = {"{", "(", "[", "<"}

    def isValid(self, s: str) -> bool:

        if not s:
            return False

        index = 0
        while index < len(s):
            if s[index] in self.opening:
                self.stack.append(s[index])
            elif not self.stack:
                return False
            elif s[index] in self.brackets and self.stack[-1] != self.brackets[s[index]]:
                return False
            elif s[index] in self.brackets and self.stack[-1] == self.brackets[s[index]]:
                self.stack.pop()


            index += 1
        if not self.stack:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "{[]}"
    s = "([)]"
    print(Solution().isValid(s))

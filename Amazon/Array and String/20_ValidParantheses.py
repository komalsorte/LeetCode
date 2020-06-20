__author__ = 'Komal Atul Sorte'
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    def isValid(self, s):
        stack = []

        matching_parantheses = {"}": "{", "]": "[", ")": "("}

        for p in s:
            if p in matching_parantheses:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != matching_parantheses[p]:
                    return False
            else:
                stack.append(p)
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "()"
    s = "()[]{}"
    s = "(]"
    s = "([)]"
    s = "{[]}"
    s = "["
    s = "]"
    print(Solution().isValid(s))

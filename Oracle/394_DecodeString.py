"""
LeetCode - Medium
"""
"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""


class Solution:
    def decodeString(self, s: str) -> str:
        s_itr = 0
        opening, closing = "[", "]"
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        stack = list()
        while s_itr != len(s):
            if s[s_itr] == closing:
                # pop till you see opening
                token = ""
                while stack[-1] != opening:
                    token = stack.pop() + token
                # pop [
                stack.pop()
                # get digits
                count = 1
                number = 0
                while stack and stack[-1] in digits:
                    number += count * int(stack.pop())
                    count *= 10

                # make string to append
                stack.append(token * number)
                # append
            else:
                stack.append(s[s_itr])
            s_itr += 1

        result = ""
        while stack:
            result = stack.pop() + result

        return result


if __name__ == '__main__':
    s = "3[a]200[bc]"
    print(Solution().decodeString(s))

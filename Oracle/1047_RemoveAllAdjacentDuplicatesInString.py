"""
LeetCode - Easy
"""
"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 

Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.

"""


class Solution:
    def removeDuplicatesPointers(self, S: str) -> str:
        # Exceeds time limit
        start, end = 0, 1
        while end < len(S):
            if S[start] == S[end]:
                S = S[0: start] + S[end + 1:]
                start = 0
                end = 1
            else:
                start += 1
                end += 1
        return S

    def removeDuplicatesStack(self, S: str) -> str:
        stack, index = [], 0

        while index < len(S):
            if len(stack) > 0 and S[index] == stack[-1]:
                stack.pop()
            else:
                stack.append(S[index])
            index += 1
        return ''.join(stack)




if __name__ == '__main__':
    S = "abbaca"
    print(Solution().removeDuplicatesStack(S))

__author__ = 'Komal Atul Sorte'
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
"""


class Solution:
    def minimumWindowSubstring(self, S, T):
        start = 0
        end = 0
        output_substring = list()
        T_temp = list(T)
        while start < len(S) and end < len(S):
            if S[end] in T_temp and len(T) == len(T_temp):
                T_temp.remove(S[end])
                start = end
            elif S[end] in T_temp:
                T_temp.remove(S[end])
            end += 1
            if len(T_temp) == 0:
                output_substring.append(S[start:end])
                start = start + 1
                end = start
                T_temp = list(T)
        if len(output_substring) == 0:
            return ""
        else:
            return min(output_substring, key=len)


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    S = "aa"
    T = "aaa"
    print(Solution().minimumWindowSubstring(S, T))

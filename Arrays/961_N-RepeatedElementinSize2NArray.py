"""
LeetCode - Easy
"""


class Solution:
    def repeatedNTimes(self, A):

        dict_A = dict()
        element = ''
        for index_1 in range(len(A)):
            if A[index_1] in dict_A:
                dict_A[A[index_1]] += 1
                element = A[index_1]
                break
            else:
                dict_A[A[index_1]] = 1
        return element

if __name__ == '__main__':
    print(Solution().repeatedNTimes([1, 2, 3, 3]))

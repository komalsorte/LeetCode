"""
LeetCode - Easy
"""
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd

if __name__ == '__main__':
    print(Solution().sortArrayByParity([3,2,1,4]))
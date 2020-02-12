"""
LeetCode - Medium
"""
class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        substring_s = ""
        count_a = A
        count_b = B
        count_a_consecutive = 0
        count_b_consecutive = 0
        if (A > 2 and B == 0):
            return "aa"
        elif (A == 0 and B > 2):
            return "bb"
        else:
            for i in range(A + B):
                if count_a >= count_b and count_a_consecutive < 2:
                    substring_s = substring_s + "a"
                    count_a = count_a - 1
                    count_a_consecutive = count_a_consecutive + 1
                    if count_b_consecutive == 2:
                        count_b_consecutive = 0
                elif count_a <= count_b and count_b_consecutive < 2:
                    substring_s = substring_s + "b"
                    count_b = count_b - 1
                    count_b_consecutive = count_b_consecutive + 1
                    if count_a_consecutive == 2:
                        count_a_consecutive = 0
                elif count_a > count_b and count_a_consecutive == 2 and count_b <= B:
                    substring_s = substring_s + "b"
                    count_b = count_b - 1
                    count_b_consecutive = count_b_consecutive + 1
                    if count_a_consecutive == 2:
                        count_a_consecutive = 0
                elif count_a < count_b and count_b_consecutive == 2 and count_a <= A:
                    substring_s = substring_s + "a"
                    count_a = count_a - 1
                    count_a_consecutive = count_a_consecutive + 1
                    if count_b_consecutive == 2:
                        count_b_consecutive = 0
            return (substring_s)

if __name__ == '__main__':
    Solution().strWithout3a3b(1, 4)

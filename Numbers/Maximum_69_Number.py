class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_s = str(num)
        for digit in range(len(num_s)):
            if num_s[digit] == '6':
                first_part = num_s[:digit]
                second_part = num_s[digit + 1: ]
                num_s = first_part + '9' + second_part
                num = int(num_s)
                return num
if __name__ == '__main__':
    Solution().maximum69Number(9669)
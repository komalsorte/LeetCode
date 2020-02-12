"""
LeetCode - Easy
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(int(length/2)):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s) - i -1] = temp

if __name__ == '__main__':
    Solution().reverseString(["h","e","q","l","o"])
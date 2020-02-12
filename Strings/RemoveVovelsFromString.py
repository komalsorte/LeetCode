"""
LeetCode - Easy
"""
class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        dictOfVowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4, 'A': 5, 'E': 6, 'I': 7, 'O': 8, 'U': 9}
        char = 0
        while len(S) != 0:
            if S[char] in dictOfVowels.keys():
                before = S[: char]
                after = S[char + 1:]
                S = before + after
                if after == '':
                    break
            else:
                if len(S) == 1 or len(S) == char + 1:
                    break
                if len(S) != 1:
                    char = char + 1
        return S


if __name__ == '__main__':
    Solution().removeVowels("leetcodeisacommunityforcoders")
    Solution().removeVowels("aeiou")
    Solution().removeVowels("njto")

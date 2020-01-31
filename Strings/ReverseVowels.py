class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        dictOfVowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4, 'A': 5, 'E': 6, 'I': 7, 'O': 8, 'U': 9}
        arr_vowels = [None] * len(s)
        index = 0
        for i in reversed(s):
            if i in dictOfVowels.keys():
                arr_vowels[index] = i
                index = index + 1

        index = 0
        for item in range(len(s)):
            if s[item] in dictOfVowels.keys():
                after = s[item + 1:]
                before = s[:item]
                s = before + arr_vowels[index] + after
                index = index + 1
        return s


if __name__ == '__main__':
    Solution().reverseVowels("hello")

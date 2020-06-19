__author__ = 'Komal Atul Sorte'
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack, needle):
        if (haystack == "" and needle == "") or (needle == ""):
            return 0
        if haystack == "":
            return -1
        start, current = 0, 0
        needle_index = 0
        while start != len(haystack):
            if needle[needle_index] == haystack[current]:
                needle_index += 1
                current += 1
                if needle_index == len(needle):
                    return start
                if current == len(haystack):
                    break
            else:
                start += 1
                current = start
                needle_index = 0
        return -1



if __name__ == '__main__':
    haystack = "mississippi"
    needle = "issip"
    print(Solution().strStr(haystack, needle))

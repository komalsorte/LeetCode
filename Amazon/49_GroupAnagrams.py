__author__ = 'Komal Atul Sorte'
"""
Given an array of strings, group anagrams together.
"""


class Solution:
    def groupAnagrams(self, strs):
        strs_res = dict()
        for s in strs:
            s_temp = tuple(s)
            s_temp = tuple(sorted(s_temp))
            if s_temp in strs_res.keys():
                strs_res[s_temp] = strs_res[s_temp] + [s]
            else:
                strs_res[s_temp] = [s]
        return list(strs_res.values())



if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

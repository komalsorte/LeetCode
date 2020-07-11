__author__ = "Komal Atul Sorte"
"""

"""

import collections


class AutocompleteSystem:

    def __init__(self, sentences, times):
        count = collections.Counter()
        for i in range(len(sentences)):
            count[sentences[i]] = times[i]
        print(count)

    def input(self, c):
        pass


# Your AutocompleteSystem object will be instantiated and called as such:
sentences = ["i love you", "island", "ironman", "i love leetcode"]
times = [5, 3, 2, 2]
obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

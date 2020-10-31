"""
LeetCode - Medium
"""
import collections

"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
import heapq

class Solution:
    def topKFrequent2(self, words, k: int):
        map = dict()
        for w in words:
            if w in map:
                map[w] += 1
            else:
                map[w] = 1
        print(map)
        count = collections.Counter(words)
        print(count)
        # print(sorted(map.items()))
        sorted(map.items(), key=lambda item: (-item[1], item[0]))
        print(map)
        return heapq.nlargest(k, map.keys(), key=map.get)

    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        print(count)
        heap = [(-freq, word) for word, freq in count.items()]
        print(heap)
        heapq.heapify(heap)
        print(heap)
        # for _ in range(k):
        #     print(heapq.heappop(heap))
        # return [heapq.heappop(heap)[1] for _ in range(k)]
        return heapq.nlargest(k, heap)


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    print(Solution().topKFrequent(words, k))

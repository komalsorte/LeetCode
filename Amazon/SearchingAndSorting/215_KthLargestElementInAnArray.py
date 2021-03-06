__author__="Komal Atul Sorte"
"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""
import heapq
class Solution:
    def findKthLargest_Sorting(self, nums, k):
        nums.sort(reverse=True)
        print(nums)

        return nums[k - 1]
    def findKthLargest_Heapq(self, nums, k):
        klarge = heapq.nlargest(k, nums)
        return klarge[len(klarge) - 1]

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    print(Solution().findKthLargest_Heapq(nums, k))
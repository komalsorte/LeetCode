__author__ = "Komal Atul Sorte"
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


# LEETCODE
class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        # intervals.sort(key=lambda x: x[0])
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                print(merged[-1])
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

        # EXCEEDS TIME
        # updated = []
        # index = 0
        # while index < len(intervals) - 1:
        #     if intervals[index][1] >= intervals[index + 1][0]:
        #         # intervals[index] = [intervals[index][0], max(intervals[index + 1][1],intervals[index][1])]
        #         # intervals.remove(intervals[index + 1])
        #         inter = [intervals[index][0], max(intervals[index + 1][1], intervals[index][1])]
        #         if inter in updated:
        #             index += 1
        #         else:
        #             updated.append(inter)
        #         print(updated)
        #     else:
        #         index += 1
        # return updated


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 4], [4, 5]]
    intervals = [[1, 4], [0, 4]]
    intervals = [[1, 2], [2, 3], [3, 6]]
    print(Solution().merge(intervals))

__author__ = "Komal Atul Sorte"

import collections

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = collections.defaultdict(list)
        outdegree = collections.defaultdict(list)

        print(prerequisites)
        for course, prereq in prerequisites:
            indegree[course].append(prereq)
            outdegree[prereq].append(course)

        visited = 0
        indegree_zero = list()
        for course in range(numCourses):
            if course not in indegree:
                indegree_zero.append(course)
                visited += 1


        while indegree_zero:
            node = indegree_zero.pop()
            for course in outdegree[node]:
                indegree[course].remove(node)
                if indegree[course] == []:
                    indegree_zero.append(course)
                    visited += 1
        return visited == numCourses


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0]]
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    numCourses = 3
    prerequisites = [[2, 0], [2, 1]]
    print(Solution().canFinish(numCourses=numCourses, prerequisites=prerequisites))

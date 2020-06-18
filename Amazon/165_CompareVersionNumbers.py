__author__ = 'Komal Atul Sorte'
"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.
"""


class Solution:
    def compareVersion(self, version1, version2):
        version1 = version1.split(".")
        version2 = version2.split(".")

        diff = len(version1) - len(version2)
        if diff < 0:
            for d in range(abs(diff)):
                version1.append('0')
        elif diff > 0:
            for d in range(diff):
                version2.append('0')

        for ele in range(len(version1)):
            if int(version1[ele]) != int(version2[ele]):
                if int(version1[ele]) > int(version2[ele]):
                    return 1
                else:
                    return -1
        return 0


if __name__ == '__main__':

    version1 = "0.1"
    version2 = "1.1"
    version1 = "1.0.1"
    version2 = "1"
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    version1 = "1.01"
    version2 = "1.001"
    version1 = "1.0"
    version2 = "1.0.0"
    version1 = "1"
    version2 = "1.1"
    print(Solution().compareVersion(version1, version2))

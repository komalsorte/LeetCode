__author__ = 'Komal Atul Sorte'
"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
"""


"""
FAILED TEST CASE:
"2147483648"
Output:
2147483648
Expected:
2147483647
"""


class Solution:
    def myAtoi(self, sstr):
        sstr = sstr.strip()
        if len(sstr) == 0:
            return 0
        start = 0
        total = 0
        if sstr[0] == "+" or sstr[0] == "-":
            start = 1
        for i in range(start, len(sstr)):
            if sstr[i].isnumeric() and total == 0:
                total = int(sstr[i])
            elif sstr[i].isnumeric():
                total = 10 * total + int(sstr[i])
            else:
                break
        if total == 0:
            return 0
        elif total > pow(2, 31):
            return -1 * pow(2, 31)
        elif sstr[0] == "-":
            total = sstr[0] + str(total)
        return total


if __name__ == '__main__':
    sstr = "  -42"
    print(Solution().myAtoi(sstr))

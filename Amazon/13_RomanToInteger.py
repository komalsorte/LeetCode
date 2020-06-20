__author__ = 'Komal Atul Sorte'
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. 
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:

    def romanToInt(self, roman):
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        sum, i = 0, 0
        while i < len(roman):

            if (i + 1) < len(roman) and roman[i] + roman[i + 1] in roman_dict.keys():
                sum += roman_dict[roman[i] + roman[i + 1]]
                i += 2
            elif roman[i] in roman_dict.keys():
                sum += roman_dict[roman[i]]
                i += 1

        return sum

    def romanToInt1(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total


if __name__ == '__main__':
    num = "MCMXCIV"
    num = "MDCCCCXCIV"
    print(Solution().romanToInt1(num))

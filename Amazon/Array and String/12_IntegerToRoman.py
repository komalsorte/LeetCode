__author__ = 'Komal Atul Sorte'
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def intToRoman(self, num):
        roman_dict = {
            1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 4: "IV", 9: "IX", 40: "XL", 90: "XC",
            400: "CD", 900: "CM"
        }
        output = ""
        index = 1
        print(len(str(num)))
        for i in range(len(str(num))):
            digit = int(num % 10)
            num = int(num / 10)
            if digit * index in roman_dict.keys():
                output = roman_dict[digit * index] + output
            else:
                if digit > 5:
                    part_digit = digit - 5
                    output = roman_dict[5 * index] + roman_dict[index] * part_digit + output
                else:
                    output = roman_dict[index] * digit + output
            index *= 10
        return output


if __name__ == '__main__':
    num = 70
    print(Solution().intToRoman(num))

__author__ = 'Komal Atul Sorte'
"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1
"""


class Solution:
    def numberToWords(self, num):
        thousand = False
        # million = False
        # billion = False

        num = "{:,}".format(num)
        num_list = num.split(",")
        for item in num_list:
            item = int(item) % 10
            item_string = self.ones(item)
            item = item % 10
            item_string = self.tens(item)
            item = item % 10
            item_string = self.hundreds(item)


    def ones(self, num):
        switch_case = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return switch_case.get(num)

    def tens(self, num):
        switch_case = {
            1: 'Ten',
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return switch_case.get(num)

    def below20(self, num):
        switch_case = {
            1: 'Eleven',
            2: 'Twelve',
            3: 'Thirteen',
            4: 'Fourteen',
            5: 'Fifteen',
            6: 'Sixteen',
            7: 'Seventeen',
            8: 'Eighteen',
            9: 'Nineteen'
        }
        return switch_case.get(num)


if __name__ == '__main__':
    num = 222
    print(Solution().numberToWords(num))

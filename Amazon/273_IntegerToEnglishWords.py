__author__ = 'Komal Atul Sorte'
"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1
"""


class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        result_full = ""
        num = "{:,}".format(num)
        num_list = num.split(",")
        num_list.reverse()

        for item in range(len(num_list)):
            result = ""
            digits = num_list[item]

            units = int(digits) % 10
            digits = int(digits) / 10
            tens = int(digits) % 10
            digits = int(digits) / 10
            if tens == 1:
                result = self.below20(str(tens) + str(units)) + " " + result
            else:
                if units != 0:
                    result = self.ones(units) + " " + result
                if tens != 0:
                    result = self.tens(tens) + " " + result
            if int(digits) % 10 != 0:
                result = self.ones(int(digits) % 10) + " Hundred " + result
            if item == 1 and result != "":
                result = result + "Thousand "
            if item == 2 and result != "":
                result = result + "Million "
            if item == 3 and result != "":
                result = result + "Billion "
            result_full = result + result_full

        return result_full.rstrip()

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
        return switch_case.get(num, '')

    def tens(self, num):
        num = int(num)
        switch_case = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return switch_case.get(num, '')

    def below20(self, num):
        num = int(num)
        switch_case = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return switch_case.get(num, '')

if __name__ == '__main__':
    num = 10000000
    print(Solution().numberToWords(num))

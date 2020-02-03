# EBAY QUESTION
def reverseDigitsInPairs(n):
    # convert integer to string
    count = 0
    nums = str(n)
    i=0
    while i < len(nums):
        if i == len(nums) - 1:
            break
        current = nums[i]
        swap_with = nums[i+1]
        before = nums[:i]
        after=nums[i+2:]
        nums = before + swap_with + current + after

        i = i+2
    return int(nums)

if __name__ == '__main__':
    n = 12345
    reverseDigitsInPairs(n)


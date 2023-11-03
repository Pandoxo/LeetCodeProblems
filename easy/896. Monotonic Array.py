class Solution(object):
    def isMonotonic(self, nums):
        n = len(nums)
        isIncreasing = True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                isIncreasing = False
                break
        isDecreasing = True
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                isDecreasing = False
                break
        return isIncreasing or isDecreasing


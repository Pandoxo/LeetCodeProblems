class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        for i in range(len(arr)-1):
            if i == 0:
                diff = abs(arr[1] - arr[0])
            if abs(arr[i] - arr[i+1]) != diff:
                return False
        return True

class Solution(object):
    def arraySign(self, nums):
        negative = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                negative +=1
        if negative % 2 == 0:
            return 1
        return -1

ob = Solution()
print(ob.arraySign([-1,-2,-3,-4,3,2,1]))
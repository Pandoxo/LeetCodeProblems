class Solution(object):
    def moveZeroes(self, nums):
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums

ob = Solution()
print(ob.moveZeroes([0,1,0,3,12]))
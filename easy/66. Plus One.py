class Solution(object):
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10,len(digits)-i-1)
        num += 1
        result = []
        while num > 0:
            result.append(num%10)
            num//=10
        return result[::-1]

# class Solution(object):
#     def plusOne(self, digits):
#         digits[-1] += 1
#         i = len(digits) -1
#         result = []
#         while i>-1:
#             if digits[i] == 10:
#                 if i == 0:
#                    digits[i] = 0
#                    digits.insert(0,1)
#                 else:
#                     digits[i] = 0
#                     digits[i-1] += 1
#             i -= 1
#         return digits
ob = Solution()
print(ob.plusOne([4,3,2,1]))
class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        inum1 = 0
        inum2 = 0
        for i in range(len(num1)):
            inum1 += int(num1[i]) * pow(10,len(num1)-i-1)
        for i in range(len(num2)):
            inum2 += int(num2[i]) * pow(10,len(num2)-i-1)
        m = inum2 * inum1
        result = ""
        while m > 0:
            result += chr(m%10+48)
            m //= 10
        return result[::-1]







ob = Solution()
print(ob.multiply("123", "456"))
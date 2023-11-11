class Solution(object):
    def addBinary(self, a, b):
        result = ""
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a

        carry = 0
        for i in range(len(a) - 1, -1, -1):
            x = int(a[i]) + int(b[i]) + carry
            if x == 0:
                result += "0"
                carry = 0
            elif x == 1:
                result += "1"
                carry = 0
            elif x == 2:
                result += "0"
                carry = 1
            else:
                result += "1"
                carry = 1
        if carry:
            result += "1"

        return result[::-1]


ob = Solution()
print(ob.addBinary("11", "1"))

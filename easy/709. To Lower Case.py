# class Solution(object):
#     def toLowerCase(self, s):
#         return lower(s)

class Solution(object):
    def toLowerCase(self, s):
        result = ""
        for i in range(len(s)):
            if 64 < ord(s[i]) < 91:
                result += chr(ord(s[i]) + 32)
            else:
                result += s[i]
        return result


ob = Solution()
print(ob.toLowerCase("ABCccdeF"))


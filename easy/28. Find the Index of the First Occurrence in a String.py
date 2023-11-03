class Solution(object):

    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            count = 0
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
ob = Solution()
print(ob.strStr("aaa","aaaa"))
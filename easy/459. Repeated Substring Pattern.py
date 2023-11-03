class Solution(object):
    def repeatedSubstringPattern(self, s):

        pattern = ""
        for i in range(len(s)//2):
            pattern += s[i]
            result = ""
            while len(result) < len(s)+1:
                result += pattern
                if result != s[:len(result)]:
                    break
                else:
                    if result == s:
                        return True
        return False

ob = Solution()
print(ob.repeatedSubstringPattern("ababc"))
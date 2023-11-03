class Solution(object):
    def findTheDifference(self, s, t):
        letters_s = [0 for i in range(26)]
        letters_t = [0 for i in range(26)]

        i = 0
        while i < len(s):
            letters_s[ord(s[i]) - 97] += 1
            letters_t[ord(t[i]) - 97] += 1
            i += 1
        letters_t[ord(t[i]) - 97] += 1
        for j in range(26):
            if letters_s[j] != letters_t[j]:
                return chr(j + 97)


ob = Solution()
print(ob.findTheDifference("abcd","abcde"))
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        letters_s = [0 for i in range(26)]
        letters_t = [0 for i in range(26)]
        for i in range(len(s)):
            letters_s[ord(s[i])-97] += 1
            letters_t[ord(t[i]) - 97] += 1
        for i in range(26):
            if letters_s[i] != letters_t[i]:
                return False
        return True


ob = Solution()
print(ob.isAnagram("anagram", "nagaram"))
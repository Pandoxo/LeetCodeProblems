class Solution(object):
    def romanToInt(self, s):
        Roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        n = len(s)
        for i in range(n-1):
            if Roman[s[i]] < Roman[s[i+1]]:
                result -= Roman[s[i]]
            else:
                result += Roman[s[i]]
        result += Roman[s[n-1]]

        return result

ob = Solution()
print(ob.romanToInt("MCMXCIV"))
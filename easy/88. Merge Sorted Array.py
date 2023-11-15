class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0
        result = []
        while True:
            if i == m - 1:
                result.append(nums2[j])
                j += 1
                continue
            if j == n - 1:
                result.append(nums1[i])
                i += 1
                continue

            if j == n - 1 and i == m - 1:
                return result


ob = Solution()
print(ob.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

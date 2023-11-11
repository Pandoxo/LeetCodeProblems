class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result = []
        i,j = 0,0
        while i < len(list1):
            while j < len(list2):
                if list1[i] > list2[j]:
                    result.append(list2[j])
                    j +=1
                elif list1[i] == list2[j]:
                    result.append(list1[i])
                    result.append(list2[j])
                    i +=1
                    j +=1
                else:
                    result.append(list1[i])
                    i +=1
        return result


ob = Solution()
print(ob.mergeTwoLists([1,2,4],[1,3,4]))
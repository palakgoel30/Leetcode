class Solution:
    def frequencySort(self, s: str) -> str:
        dict1,str1 = {},''
        for i in s:
            j = ord(i)
            if(j in dict1):
                dict1[j] +=1
            else:
                dict1[j] = 1
        sorted_dict = sorted(dict1.items(),key=lambda x:x[1],reverse=True)
        for i in range(len(sorted_dict)):
            str1 += chr(sorted_dict[i][0])*sorted_dict[i][1]
        return str1
s = 'tree'
obj = Solution()
print(obj.frequencySort(s))
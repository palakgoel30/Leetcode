class Solution:
    def getRow(self, rowIndex: int):
        List1 = []
        for i in range(rowIndex + 1):
            temp_list = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    temp_list.append(1)
                else:
                    temp_list.append(List1[i - 1][j - 1] + List1[i - 1][j])
            List1.append(temp_list)
        temp_list = []
        return List1[rowIndex]

rowIndex = 5
obj = Solution()
print(obj.getRow(rowIndex))
def generate(numRows):
    list1 = []
    for i in range(numRows):
        temp_list = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                temp_list.append(1)
            else:
                temp_list.append(list1[i - 1][j - 1] + list1[i - 1][j])
        list1.append(temp_list)
    return list1

numRows = 5
print(generate(numRows))
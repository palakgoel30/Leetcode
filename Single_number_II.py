def singleNumber(nums):
    dict = {}
    for item in nums:
        if (item in dict):
            dict[item] += 1
        else:
            dict[item] = 1
    for key, value in dict.items():
        if (value == 1):
            return key


nums = [2, 2, 3, 2]
print(singleNumber(nums))

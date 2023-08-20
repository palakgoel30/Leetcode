def peakIndexInMountainArray(arr):
    length = len(arr)
    if(length >=3):
        for i in range(0,length):
            if(arr[i]< arr[i+1]):
                i+=1
            else:
                break
    return i

arr = [0,10,5,2]
print(peakIndexInMountainArray(arr))
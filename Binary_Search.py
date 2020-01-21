data = [21,12,32,43,54,23,12,4,53,21,11,9,5,8,10,71,32]

def binary_search_iterative(data, val, l, h):
    data.sort()
    print(data)
    while l <= h:
        mid = round(l + (h - 1)/2) #Find Middle Index

        if data[mid] == val:
            return mid
        elif val <= data[mid]:
            h = mid - 1
        elif val >= data[mid]:
            l = mid + 1    
    return -1

index = binary_search_iterative(data, 11, 0, len(data) - 1)
print("Element found at index",index)






    
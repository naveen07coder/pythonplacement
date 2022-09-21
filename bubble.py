# def bubble(array):
#
#     arr = array
#     n = len(arr)
#
#     for i in range(n):
#
#         for j in range(0, n-i-1):
#
#             if arr[j] > arr[j+1]:
#
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#     return arr


# def bubble(array):
#     for i in range(len(array)):
#         for j in range(0, len(array)-0-1):
#             if array[j]>array[j+1]:
#                 array[j], array[j+1] = array[j+1],array[j]
#
#     return array

def bubble(arr):
    array = arr
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [12,324,453,21,342,644,245,88, 67]
print(bubble(array))
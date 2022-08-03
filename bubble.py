def bubble(array):

    arr = array
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

array = [12,324,453,21,342,644,245,88, 67]

print(bubble(array))
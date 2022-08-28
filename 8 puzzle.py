
def get_idx(arr ,i ,j):
    n = len(arr)
    res = []

    if 0<= i + 1 < n and 0 <= j < n:
        res.append((i + 1, j))
    if 0 <= i - 1 < n and 0 <= j < n:
        res.append((i - 1, j))
    if 0 <= i < n and 0 <= j + 1 < n:
        res.append((i, j + 1))
    if 0 <= i < n and 0 <= j - 1 < n:
        res.append((i, j - 1))

    return res


def depth_limited_search(arr, target, limit, i, j):
    # print(arr)
    if arr == target:
        return True
    if limit == 0:
        return False

    ans = False
    for idx_x, idx_y in get_idx(arr, i, j):
        arr[i][j], arr[idx_x][idx_y] = arr[idx_x][idx_y], arr[i][j]
        ans = ans or depth_limited_search(arr, target, limit - 1, idx_x, idx_y)
        arr[i][j], arr[idx_x][idx_y] = arr[idx_x][idx_y], arr[i][j]

    return ans


arr = [[2, 8, 3], [1, 6, 4], [7, None, 5]]
target = [[2, 8, 3], [6, 7, 4], [1, None, 5]]
limit = 43
if depth_limited_search(arr, target, limit, 2, 1):
    print("possible")
else:
    print("not possible")

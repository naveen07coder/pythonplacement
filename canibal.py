def bfs(n):
    arr = []
    q = [[(0, 0, n, n, True), arr]]
    vis = set()

    while q:

        ele_cur = q.pop(0)
        ele, arr = ele_cur
        if ele[0] == n and ele[1] == n and ele[2] == 0 and ele[3] == 0:
            return arr
        if (ele[1] > 0 and ele[0] > ele[1]) or (ele[3] > 0 and ele[2] > ele[3]):
            continue
        if ele[0] < 0 or ele[0] > n or ele[1] < 0 or ele[1] > n or ele[2] < 0 or ele[2] > n or ele[3] < 0 and ele[3] > n:
            continue

        vis.add(ele)

        if ele[4]:
            if (ele[0] + 1, ele[1], ele[2] - 1, ele[3], not ele[4]) not in vis:
                q.append([(ele[0] + 1, ele[1], ele[2] - 1, ele[3], not ele[4]), arr + ["<--1 canni"]])

            if (ele[0] + 2, ele[1], ele[2] - 2, ele[3], not ele[4]) not in vis:
                q.append([(ele[0] + 2, ele[1], ele[2] - 2, ele[3], not ele[4]), arr + ["<--2 canni"]])

            if (ele[0], ele[1] + 1, ele[2], ele[3] - 1, not ele[4]) not in vis:
                q.append([(ele[0], ele[1] + 1, ele[2], ele[3] - 1, not ele[4]), arr + ["<--1 missi"]])

            if (ele[0], ele[1] + 2, ele[2], ele[3] - 2, not ele[4]) not in vis:
                q.append([(ele[0], ele[1] + 2, ele[2], ele[3] - 2, not ele[4]), arr + ["<--2 missi"]])

            if (ele[0] + 1, ele[1] + 1, ele[2] - 1, ele[3] - 1, not ele[4]) not in vis:
                q.append([(ele[0] + 1, ele[1] + 1, ele[2] - 1, ele[3] - 1, not ele[4]), arr + ["<--1 canii 1 missi"]])

        else:
            if (ele[0] - 1, ele[1], ele[2] + 1, ele[3], not ele[4]) not in vis:
                q.append([(ele[0] - 1, ele[1], ele[2] + 1, ele[3], not ele[4]), arr + ["1 canni -->"]])

            if (ele[0] - 2, ele[1], ele[2] + 2, ele[3], not ele[4]) not in vis:
                q.append([(ele[0] - 2, ele[1], ele[2] + 2, ele[3], not ele[4]), arr + ["2 canni -->"]])

            if (ele[0], ele[1] - 1, ele[2], ele[3] + 1, not ele[4]) not in vis:
                q.append([(ele[0], ele[1] - 1, ele[2], ele[3] + 1, not ele[4]), arr + ["1 missi -->"]])

            if (ele[0], ele[1] - 2, ele[2], ele[3] + 2, not ele[4]) not in vis:
                q.append([(ele[0], ele[1] - 2, ele[2], ele[3] + 2, not ele[4]), arr + ["2 missi -->"]])

            if (ele[0] - 1, ele[1] - 1, ele[2] + 1, ele[3] + 1, not ele[4]) not in vis:
                q.append([(ele[0] - 1, ele[1] - 1, ele[2] + 1, ele[3] + 1, not ele[4]), arr + ["1 canni 1 missi -->"]])


for i in bfs(3):
    print(i)

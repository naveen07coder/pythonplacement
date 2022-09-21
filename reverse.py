# A= [1, 2, 3, 4, 5]
# l = []
# # for i in range(len(A)):
# #     for j in range(len(A)):
# #         if A[-1] == 0:
# #             break
# #         else:
# #             l.append(A.pop())
# # print(l)
#


r = [[2,1],
     [2,1]]

c = [[1,2],
     [2,1]]

res = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

for i in range(len(r)):
    for j in range(len(c[0])):
        for k in range(len(c)):
            res[i][j] += r[i][j] * c[i][j]

for r in res:
    print(r)
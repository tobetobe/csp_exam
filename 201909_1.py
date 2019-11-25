# 试题编号：	201909-1
# 试题名称：	小明种苹果
# 时间限制：	2.0s
# 内存限制：	512.0MB
from functools import reduce


def sum(x, y):
    return x + y


N, M = map(lambda x: int(x), input().split(' '))
a = []

for n in range(N):
    a.append(map(lambda x: int(x), input().split(' ')))

T = 0
k = 0
P = 0
for index, item in enumerate(a, start=1):
    item = list(item)
    # print(index, item)
    cut_sum = 0
    for num in item:
        cut_sum = cut_sum + num
    T = cut_sum + T
    if cut_sum > k:
        k = index
        P = abs(reduce(sum, item[1:]))

print('{} {} {}'.format(T, k, P))

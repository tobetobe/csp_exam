def mid_num(num_list, length):
    if n % 2 == 0:
        result = (num_list[int(n/2)]+num_list[int(n/2 - 1)])/2
        return int(result) if int(result) == result else result
    else:
        return num_list[int((n-1)/2)]


n = int(input())
num_list = list(map(lambda n: int(n), input().split(' ')))
print(max(num_list), mid_num(num_list, n), min(num_list))

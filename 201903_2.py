n = int(input())
string_list = []

for i in range(1, n+1):
    string_list.append(input().strip())


for item in string_list:
    # calc
    stack = []
    for word in item:
        if word in ['x', '/', '+', '-']:  # is number
            stack.append(word)
        else:
            if len(stack) > 0:
                if stack[-1] == 'x':
                    stack.pop()
                    result = int(stack.pop()) * int(word)
                    stack.append(result)
                elif stack[-1] == '/':
                    stack.pop()
                    result = int(int(stack.pop()) / int(word))
                    stack.append(result)
                else:
                    stack.append(int(word))
            else:
                stack.append(int(word))
    # print(stack)
    sum = stack[0]
    for index, item in enumerate(stack):
        # print(item, index)
        if item == '+':
            sum = sum + int(stack[index + 1])
        elif item == '-':
            sum = sum - int(stack[index + 1])
    # print(sum)

    if sum == 24:
        print("Yes")
    else:
        print("No")

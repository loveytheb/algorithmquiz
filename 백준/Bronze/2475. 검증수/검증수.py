num_list = list(map(int, input().split()))

result = 0

for i in num_list:
    result += i**2

total_result = result % 10

print(total_result)
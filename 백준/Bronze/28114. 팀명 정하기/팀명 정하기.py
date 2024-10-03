import sys
input = sys.stdin.readline

year = []
problem_name = []

for _ in range(3):
    P, Y, S = input().split()
    year.append(int(Y))
    problem_name.append([int(P), S])

year.sort()
problem_name.sort(reverse=True)

first_teamName = ""
second_teamName = ""

for i in range(3):
    first_teamName += str(year[i] % 100)
    second_teamName += problem_name[i][1][0]

print(first_teamName)
print(second_teamName)
import sys
input = sys.stdin.readline

X = input().strip()
count = 0

while len(X) > 1: # 한 자리 숫자가 아닐 때 반복
    count += 1
    total = 0
    for i in X:  # 문자열이므로 각 자릿수 접근
        total += int(i) # 각 자릿수 합산
    X = str(total) # 합계를 문자열로 변환

print(count)

# 최종 결과가 3의 배수인지 확인
if int(X) % 3 == 0:
    print("YES")
else:
    print("NO")

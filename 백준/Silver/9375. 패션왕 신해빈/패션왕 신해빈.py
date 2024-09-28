import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    n = int(input()) # 의상 수
    clothes_dic = {} # 의상의 종류를 key, 의상 이름을 value로 저장
    
    for _ in range(n):
        name, category = input(). split()
        if category in clothes_dic: # category가 dic에 존재하면
            clothes_dic[category].append(name) # 해당 리스트에 name 추가
        else: # 존재하지 않으면
            clothes_dic[category] = [name] # 새로운 리스트 생성하여 해당 의상 이름 추가
    
    count = 1 # 각 의상의 종류에 대해 곱해주어야 하기 때문에 초기값을 1로 설정
    
    for i in clothes_dic.values(): # 의상의 종류별 리스트 반복
        count *= len(i) + 1 # 종류별 의상 수 + 1 (선택하지 않는 경우)
    
    print(count - 1) # 알몸인 경우 제외하기 위해서 1 빼기
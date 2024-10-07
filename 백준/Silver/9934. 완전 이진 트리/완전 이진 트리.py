import sys
import math

input = sys.stdin.readline  # 빠른 입력을 위한 함수

def build_complete_binary_tree(nodes):
    # 주어진 노드 수에 따른 완전 이진 트리의 높이를 계산
    height = math.ceil(math.log2(len(nodes) + 1)) - 1  # log2는 이진 트리의 높이를 구함
    levels = [[] for _ in range(height + 1)]  # 각 레벨을 저장할 리스트 초기화 (높이 + 1)

    # 현재 서브트리를 채우기 위한 재귀 함수 정의
    def fill_levels(start, end, level):
        if start > end:  # 시작 인덱스가 끝 인덱스를 초과하면 종료
            return
        mid = (start + end) // 2  # 중간 인덱스 계산
        levels[level].append(nodes[mid])  # 중간 노드를 현재 레벨에 추가
        # 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 채움
        fill_levels(start, mid - 1, level + 1)  # 왼쪽 서브트리 (start ~ mid-1)
        fill_levels(mid + 1, end, level + 1)  # 오른쪽 서브트리 (mid+1 ~ end)

    fill_levels(0, len(nodes) - 1, 0)  # 트리 구성 시작 (전체 범위와 첫 번째 레벨)

    # 각 레벨에 저장된 노드 값을 출력
    for level in levels:  # levels 리스트를 순회
        print(' '.join(map(str, level)))  # 리스트를 공백으로 구분하여 출력

# 입력 처리
n = int(input().strip())  # 노드의 개수를 입력받음
nodes = list(map(int, input().strip().split()))  # 노드 값들을 리스트로 입력받음

# 완전 이진 트리를 구성하고 출력
build_complete_binary_tree(nodes)
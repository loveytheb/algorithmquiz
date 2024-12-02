from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
queue = deque()
stack = []

for _ in range(n):
    command = input().strip().split()
    if command[0] == '1':
        queue.append(command[1])
        stack.append('back')
    elif command[0] == '2':
        queue.appendleft(command[1])
        stack.append('front')
    elif command[0] == '3':
        if stack:
            if stack.pop() == 'back':
                queue.pop()
            else:
                queue.popleft()

print(''.join(queue) if queue else '0')
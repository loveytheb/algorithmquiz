import sys
input = sys.stdin.readline

N, M = map(int, input().split())
song_dic = {}

for _ in range(N):
    song = input().strip().split() # 노래 정보 입력
    sound = ''.join(song[2:5]) # 첫 세 음 합치기

    if sound in song_dic:
        song_dic[sound] = '?' # 중복된 음일 경우 '?'로 설정
    else:
        song_dic[sound] = song[1] # 노래 제목 저장

for _ in range(M):
    sound = ''.join(input().split())

    if sound in song_dic:
        print(song_dic[sound]) # 해당 음이 있을 경우 제목 또는 '?' 출력
    else:
        print('!') # 해당 음이 없을 경우 '!' 출력

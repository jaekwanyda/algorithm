import sys
input = sys.stdin.readline
#아이디어: greedy 문제 처럼 보인다. 핀 꽃이 지는 순간 가장 길게 펴있을 수 있는 꽃을 고르면 된다.
#n 입력받기
n = int(input())
#꽃 정보 입력받기
flower = [[100*i+j for j in range(32)] for i in range(13)]
array = []
for _ in range(n):
    s_m,s_d,e_m,e_d = map(int,input().split())
    s = s_m*100+s_d; e = e_m*100+e_d
    array.append((s,e))
array = sorted(array,key= lambda x: (x[0],-x[1]))
max_m = 0; max_d = 0; max_m_d = 0
for s,e in array:
    if e>max_m_d:
        max_m_d = e
        #시작 날짜 부터 끝나는 날짜까지 피는 최대 날짜로 바꿔주기
        s_m,s_d,e_m,e_d = s//100,s%100,e//100,e%100
        k = e_m*100+e_d
        for i in range(s_d,32):
            flower[s_m][i] = max(flower[s_m][i],k)
        for i in range(s_m+1,e_m+1):
            for j in range(1,32):
                flower[i][j] = max(flower[i][j],k)
#3월 1일 부터 11월 30일 까지 조사하기
start = flower[3][1]
n = 1
while True:
    if start>1130:
        print(n)
        break
    start_m, start_d = start//100, start%100
    start = flower[start_m][start_d]
    if start == start_m*100+start_d:
        print(0)
        break
    n += 1
        

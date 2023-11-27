import sys
input = sys.stdin.readline
#아이디어: 서류심사로 먼저 정렬 후에 하나씩 내려가면서 자기보다 낮으면 탈락시키자
t = int(input())
for _ in range(t):
    n = int(input())
    interview_score = [0]*(n+1)
    for _ in range(n):
        a,score = map(int,input().split())
        interview_score[a] = score
    start_score = interview_score[1]
    result = n
    for i in range(1,n+1):
        if interview_score[i] > start_score:
            result -= 1
        start_score = min(start_score,interview_score[i])
    print(result)
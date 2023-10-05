import sys
input = sys.stdin.readline
#아이디어: 그냥 dict 문제 같다
#n,m 입력받기
n,m = map(int,input().split())
#포켓몬 정보 입력받기
po_dict = {}
for i in range(1,n+1):
    poketmon = input().rstrip()
    po_dict[poketmon] = i
    po_dict[str(i)] = poketmon
for _ in range(m):
    ask = input().rstrip()
    print(po_dict[ask])
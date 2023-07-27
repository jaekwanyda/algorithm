import sys
input = sys.stdin.readline
#아이디어: find,union으로 2개의 집합 찾고 그 집합 주인공 2명 출력하기
#n입력받기
n = int(input())
parent = [i for i in range(n+1)] #처음엔 자기 자신이 부모
#부모 노드 찾는 함수
def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
def union(a,b):
    a_p = find(a)
    b_p = find(b)
    #더 작은 수를 부모로 지정
    if a_p > b_p:
        parent[a_p] = b_p
    else:
        parent[b_p] = a_p
graph = []
for _ in range(n-2):
    a,b = map(int,input().split())
    union(a,b)
for i in range(1,n+1):
    parent[i]=find(i)
for i in range(2,n+1):
    if parent[i] != parent[i-1]:
        print(parent[i],parent[i-1])
        break
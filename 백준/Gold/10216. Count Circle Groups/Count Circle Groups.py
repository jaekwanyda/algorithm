import sys
input = sys.stdin.readline
#아이디어: union, find를 쓰면 될 것 같은데 거리 R이 애매하다. n이 최대 3000이므로 각각의 점에 대해서 계산해줘도 시간은 충분할 것 같다.
#T입력받기
t = int(input())
#각각의 테스트 케이스 별 처리해주기
def find(parent,a):
    if parent[a]==a:
        return a
    else:
        parent[a] = find(parent,parent[a])
        return parent[a]
def union(parent,a,b):
    p_a = find(parent,a); p_b = find(parent,b)
    if p_a != p_b:
        #작은 수를 부모 노드로
        if p_a < p_b:
            parent[p_b] = p_a
        else:
            parent[p_a] = p_b
for _ in range(t):
    #n입력받기
    n = int(input())
    #적군 진영 정보 입력받기
    array = []
    parent = [i for i in range(n+1)] #처음 부모노드는 자기 자신
    for i in range(1,n+1):
        nx,ny,nr = map(int,input().split())
        for idx,x_zip in enumerate(array):
            x,y,r = x_zip
            #만약 기존의 진영과 반경안에 들어오거나 겹친다면 union 해주기
            if ((x-nx)**2+(y-ny)**2) <= (r+nr)**2:
                union(parent,idx+1,i)
        array.append((nx,ny,nr))
    for i in range(1,n+1):
        parent[i] =find(parent,i)
    set_parent = set(parent)
    #0은 빼줘야 하니까 -1
    print(len(set_parent)-1)
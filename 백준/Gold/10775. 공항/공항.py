import sys
input = sys.stdin.readline
#아이디어: 그리디(도킹 가능한 최대 수 찾기)(union find  해서 가능한 가장 큰 수를 저장하도록 해보자)
def find(a):
    if plane[a]<0:
        return a
    
    plane[a]=find(plane[a])
    return plane[a]

def union(a,b): 
    a,b = find(a),find(b)

    if a==b :
        return

    plane[b]=a
    
g = int(input())
p = int(input())
plane =[-1 for _ in range(g+1)]
ans=0
for i in range(p):
    plane_gate= int(input())
    target = find(plane_gate)
    if target==0:
        break
    union(target-1, target)
    ans+=1
    
print(ans)
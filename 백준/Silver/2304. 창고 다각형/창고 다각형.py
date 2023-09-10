import sys
input = sys.stdin.readline
#아이디어: 투포인터를 써서 양쪽에서 접근하면 충분히 해결 가능해보인다.
#n 입력받기
n = int(input())
#박스 정보 입력받기
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
max_n = max(x for x,_ in array)
#박스 정보 list로 정리해주기
box = [0]*(max_n+1)
for x,h in array:
    box[x] = h
left,right = 0,max_n
max_left,max_right= box[left],box[right]
total = max_left + max_right
while left<right:
    if max_left < max_right:
        left += 1
        max_left = max(max_left,box[left])
        total += max_left
    else:
        right -= 1
        max_right = max(max_right,box[right])
        total += max_right
print(total-max_right)

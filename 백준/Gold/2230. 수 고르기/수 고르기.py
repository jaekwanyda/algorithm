import sys
input = sys.stdin.readline
#아이디어: 2포인터를 쓰면 될 것 같다. 정수를 입력받는거 주의!!
#n,m 입력받기
n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
s_idx = 0 #처음 시작 index
e_idx = 0 #움직이는 끝의 index
min_answer = 9999999999
while True:
    if e_idx == n:
        break
    if e_idx == n-1 and array[e_idx]-array[s_idx]<m:
        break
    a = array[e_idx]-array[s_idx]
    if a >= m and not e_idx==s_idx:
        s_idx += 1
        min_answer = min(min_answer,a)
    else:
        e_idx += 1
print(min_answer)
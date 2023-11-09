import sys
input = sys.stdin.readline
#아이디어: 각각의 지점에서 투포인터로 합해보자
n = int(input())
array = list(map(int,input().split()))
array.sort()
answer = 0
for idx,a in enumerate(array):
    tmp = array[:idx]+array[idx+1:]
    start = 0
    end = n-2
    target = array[idx]
    while start<end:
        tmp_sum = tmp[start]+tmp[end]
        if tmp_sum < target:
            start += 1
        elif tmp_sum > target:
            end -= 1
        else:
            answer += 1
            break
print(answer)
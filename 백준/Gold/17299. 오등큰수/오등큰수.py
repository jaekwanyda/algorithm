import sys
input = sys.stdin.readline
#아이디어: 왼쪽에서 부터 하나씩 확인해주면 될 것 같다.
import heapq
from collections import Counter
n = int(input())
array = list(map(int,input().split()))
counter = dict(Counter(array))
q = []
results = [-1]*n
for i in range(n):
    while q:
        cnt,k = heapq.heappop(q)
        if counter[array[i]] > cnt:
            results[k] = array[i]
        else:
            heapq.heappush(q,[cnt,k])
            break
    heapq.heappush(q,[counter[array[i]],i])
print(*results)
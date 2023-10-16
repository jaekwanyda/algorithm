import sys
input = sys.stdin.readline
#아이디어: left, right heapq를 이용해보자
import heapq
n = int(input())
left,right = [],[]
mid = 0
for i in range(n):
    a = int(input())
    if left and right:
        l = -heapq.heappop(left)
        r = heapq.heappop(right)
        if r < a:
            mid = r
            heapq.heappush(left,-l)
            heapq.heappush(right,a)
        elif l > a:
            mid = l
            heapq.heappush(left,-a)
            heapq.heappush(right,r)
        else:
            mid = a
            heapq.heappush(left,-l)
            heapq.heappush(right,r)
        if len(left) > len(right):
            heapq.heappush(right,mid)
            mid = -heapq.heappop(left)
            heapq.heappush(left,-mid)
        else:
            heapq.heappush(left,-mid)
    elif left:
        l = -heapq.heappop(left)
        if l < a:
            mid = l
            heapq.heappush(left,-l)
            heapq.heappush(right,a)
        else:
            mid = a
            heapq.heappush(left,-a)
            heapq.heappush(right,l)
    else:
        mid = a
        heapq.heappush(left,-a)
    print(mid)
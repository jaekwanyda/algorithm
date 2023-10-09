import sys
input = sys.stdin.readline

# n, m 입력받기
n, m = map(int, input().split())

# 강의 길이 입력받기
lectures = list(map(int, input().split()))

left, right = max(lectures), sum(lectures)

while left <= right:
    mid = (left + right) // 2
    cnt = 1  # 첫 번째 강의부터 시작하므로 cnt를 1로 초기화
    tmp = 0

    for i in range(n):
        if tmp + lectures[i] > mid:
            cnt += 1
            tmp = 0
        tmp += lectures[i]

    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)

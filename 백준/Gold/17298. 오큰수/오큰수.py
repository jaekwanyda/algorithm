def find_next_greater_elements(arr):
    n = len(arr)
    result = [-1] * n  # 초기값으로 -1을 설정

    stack = []  # 스택을 사용하여 인덱스를 저장

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            # 현재 원소가 스택의 맨 위 원소보다 크다면
            # 스택의 맨 위 원소의 오큰수를 현재 원소로 설정
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))

# 오큰수 찾기
result = find_next_greater_elements(arr)

# 결과 출력
print(*result)

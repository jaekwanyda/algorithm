def solution(numbers):
    answer = []
    def dfs(number):
        n = len(number)
        if n == 1:
            return True
        mid = n//2
        if mid == 1:
            if number[1] == '0' and (number[0] == '1' or number[2] == '1'):
                return False
            else:
                return True
        if number[mid] == '0':
            if sum(list(map(int,number))) != 0:
                return False
        left = number[:mid]
        right = number[mid+1:]
        return dfs(left) and dfs(right)
    for number in numbers:
        binary = bin(number)[2:]
        n = len(binary)
        cnt = 0
        while not all(list(map(int,bin(n + cnt)[2:]))):
            cnt += 1
        binary = cnt*'0' + binary
        answer.append(int(dfs(binary)))
    return answer
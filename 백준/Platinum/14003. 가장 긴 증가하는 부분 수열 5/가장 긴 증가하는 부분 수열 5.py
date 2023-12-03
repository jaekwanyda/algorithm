import sys
input = sys.stdin.readline
#아이디어: 일반적인 증가하는 수열은 dp를 이용하면 된다. 앞의 수 중 자기 보다 작고 가장 길이가 긴 수열을 찾아 뒤에 붙히는 방식으로 이루어진다.
#하지만 이번엔 길이가 100만이기 때문에 이 방법을 사용하면 각각의 경우 별로 앞의 모든 dp를 확인해야 해서 시간초과가 날 것이다.
#수열의 길이 중 가장 작은 값으로 list를 만들어 두자. 그리고 만들어진 list에서 이분 탐색을 통해 가능한 수 중 가장 큰 값을 찾자
n = int(input())
array = list(map(int,input().split()))
length_dict = dict()
length_dict[1] = array[0]
max_length = [0]*n
max_length[0] = 1
for i in range(1,n):
    start = 1
    end = i
    while start<=end:
        mid = (start+end)//2
        #mid길이가 존재하고 이 값이 array[i] 보다 작을 때 뒤에 붙힐 수 있다.
        if mid in length_dict and length_dict[mid] < array[i]: 
            start = mid+1
        else:
            end = mid-1
    if start in length_dict:
        length_dict[start] = min(length_dict[start],array[i])

    else:
        length_dict[start] = array[i]
    max_length[i] = start
print(max(max_length))
#제일 마지막 부터 하나하나 찾아주자
idx = max_length.index(max(max_length))
length = max(max_length)
result = []
for i in range(idx,-1,-1):
    if max_length[i] == length:
        result.append(array[i])
        length -= 1
print(*sorted(result))
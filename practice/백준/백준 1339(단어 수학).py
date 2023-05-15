from collections import defaultdict
#아이디어: defaultdict를 이용해서 나온 문자열 중 가장 큰 수가 들어온 순서대로 9~0을 부여한다.
#단어의 개수 n 입력받기
n = int(input())
#단어들 입력받기
alpha_dict = defaultdict(int)
for _ in range(n):
    s = input()
    for i in range(len(s)):
        alpha_dict[s[i]] += 10**(len(s)-i-1)
#들어온 수 대로 정렬
values = list(alpha_dict.items())
values= sorted(values,key=lambda x: -x[1])
num = 9 #시작수
result = 0
for _,value in values:
    result += value*num
    num -= 1
#출력
print(result)
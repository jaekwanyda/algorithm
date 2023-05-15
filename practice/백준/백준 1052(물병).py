#아이디어 : 단순하게 주어진 N을 이진법으로 바꾼 뒤 1의 개수를 확인한다.
#만약 개수가 k보다 많다면 이진법 자리수 중 가장 작은 자리수부터 순차적으로 더해줘 결국 1의 개수가 k와 같게 바꿔준다
#N,K 입력받기
n,k = map(int,input().split())
#이진법으로 바꿔주는 함수(!!!주의:순서 거꾸로!!!)
def second(num):
    s = []
    while num:
        a = num%2 
        s.append(a)
        num = num//2
    return s
#이진법 덧셈해주는 함수
def add_second(second_list,idx):
    if second_list[idx] == 0:
        second_list[idx] += 1
    else:
        second_list[idx] = 0
        if idx+1 < len(second_list):
            second_list = add_second(second_list,idx+1)
        else:
            second_list.append(1)
    return second_list
#n을 이진법 리스트로 바꾸기
second_n = second(n)
#1의 합이 k와 같아질 때 까지 반복
answer = 0
while sum(second_n) > k:
    for idx,i in enumerate(second_n):
        if i == 1:
            answer += 2**(idx)
            second_n = add_second(second_n,idx)
            break

#출력
print(answer)
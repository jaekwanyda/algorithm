import heapq
#아이디어: heapq를 이용해서 가장 작은 수에 모든 소수와 곱한 값을 다시 heapq에 넣어준다.
#그렇게 나온 순서대로 N번째 오는 것을 출력한다.
#K,N 입력
k,n = map(int,input().split())
#소수 리스트 입력
primes = list(map(int,input().split()))
#heapq 생성 및 모든 소수 넣기
q = []
for i in primes:
    heapq.heappush(q,i)
#n개가 나올 때 까지 heapq에서 빼고 넣기
cnt = 0
pre_tmp =0
m_cnt = 0
while cnt != n :
    tmp = heapq.heappop(q)
    #만약 전과정과 뽑은 값이 같다면 다시 뽑기
    if tmp == pre_tmp:
        continue
    if len(q) > n*2 and m_cnt == 0:
        m = max(q)
        m_cnt = 1
    if m_cnt ==1:
        for i in primes:
            if tmp*i < m:
                heapq.heappush(q,tmp*i)
    else:
        for i in primes:
            heapq.heappush(q,tmp*i)
    cnt += 1
    pre_tmp = tmp
#출력
print(tmp)
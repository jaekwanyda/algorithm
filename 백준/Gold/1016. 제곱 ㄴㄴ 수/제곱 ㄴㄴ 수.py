import sys
input = sys.stdin.readline
#아이디어: 소인수분해 후 수가 2개 겹치는게 있으면 제거해주자
start,end = map(int,input().split())
checks = [1]*int((end)**(0.5)+1)
results = {i:1 for i in range(start,end+1)}
for i in range(2,len(checks)):
    if checks[i] == 1:
        k = 2*i
        while k<len(checks):
            checks[k] = 0
            k += i
        k = i**2*(start//i**2) 
        while k<end+1:
            results[k] = 0
            k += i**2
print(sum(results.values()))
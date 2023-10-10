import sys
input = sys.stdin.readline
#아이디어: 이중분할을 이용하자
fibo_dict = {}
def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n in fibo_dict:
        return fibo_dict[n]
    if n%2 == 0:
        fibo_dict[n] = (fibo(n//2)*(2*fibo(n//2-1)+fibo(n//2))) % 1000000007
        return fibo_dict[n]
    else:
        fibo_dict[n] = (fibo((n+1)//2)**2 + fibo((n-1)//2)**2) % 1000000007
        return fibo_dict[n]
n = int(input())
print(fibo(n))
    

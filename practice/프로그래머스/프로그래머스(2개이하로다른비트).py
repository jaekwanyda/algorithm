# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

def second(n): #n을 2진수로 표현했을 때 1의 개수 구하는 함수
    sum_1=0
    while True:
        if n==1:
            sum_1+=1
            break
        elif n==0:
            break
        a=n%2
        if a==1:
            sum_1+=1
        n=n//2
    return sum_1
def solution(numbers):
    answer = []
    for number in numbers:
        if number%2==0:
            answer.append(number+1)
        else:
            k=number+1
            if second(number^k)<=2:
                answer.append(k)
            else:
                for i in range(second(number^k)-2):
                    k+=2**i
                answer.append(k)
                    
                    
    return answer

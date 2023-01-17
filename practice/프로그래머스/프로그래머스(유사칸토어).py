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

#첫번째 제출==> 시간 초과(n이 커질수록 길이가 너무 기하급수적으로 늘어난다.)
def solution(n, l, r):
    answer = 0
    contour='1'
    for i in range(n):
        new_contour=''
        for j in contour:
            if j=='1':
                new_contour+='11011'
            else:
                new_contour+='00000'
        contour=new_contour
    cnt=0
    for i in range(l-1,r+1):
        if contour[i]=='1':
            cnt+=1
    
    return cnt


# +
#두번째 제출: 각각의 요소 별로 부모노드를 찾아가며 해보려 했지만 시간초과 발생
def solution(n, l, r):
    answer = 0
    one_cnt=0
    for i in range(l-1,r):
        k=n
        while n:
            a, b = divmod(i, 5 ** (n - 1))
            if a==2:
                break
            i=b
            n-=1
            if n==0 and i!=2:
                one_cnt+=1
        n=k
        
    
    return one_cnt



#비슷한 풀이 발견
def solution(n, l, r):
    answer = r-l+1
    for num in range(l-1,r):
        while num>=1:
            a,b=divmod(num,5)
            if b==2 or a==2:
                answer-=1
                break
            num=a


    return answer


# +
#최종적으로 제출한 것
def find_one(l):
    i=1
    while True:
        if 5**i>l:
            if i>1:
                a=l//(5**(i-1))
                b=l%(5**(i-1))
                if a<2:
                    cnt=find_one(b)
                    return cnt+a*(4**(i-1))
                elif a>2:
                    cnt=find_one(b)
                    return cnt+(a-1)*(4**(i-1))
                else:
                    return 2*(4**(i-1))
                
            else:
                if l>=3:
                    return l-1
                else:
                    return l
        elif 5**i == l: 
            return 4 ** i
        else:
            i += 1
        
def solution(n, l, r):
    return find_one(r)-find_one(l-1)


# -

a=[1,2,3,5,4]
a[-3]



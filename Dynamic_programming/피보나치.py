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

# +
#아코테 연습
#재귀함수를 이용한 하향식 방법(탑다운)
d=[0]*100

def pibo(x):
    if x==1 or x==2:
        d[x]=1
    if d[x]!=0:
        return d[x]
    else:
        d[x]=pibo(x-1)+pibo(x-2)
        return d[x]
    
print(pibo(3))
        

# +
#반복문을 이용한 상향식 방법(바텀업)
d=[0]*100
d[1]=1
d[2]=1
for i in range(3,len(d)): #1,2를 설정해 두어서 3부터 시작
    d[i]=d[i-1]+d[i-2]
    
print(d[99])
# -



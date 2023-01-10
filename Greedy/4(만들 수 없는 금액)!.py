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
#이코테 실전 4
#아이디어: 굉장히 떠올리기 힘들었다. 답지를 참고한 결과 세부 과정은 이렇다
#1. 동전 금액을 정렬한다. 2.동전을 하나씩 늘려가며 만들 수 있는 최소 금액을 늘려간다.
n=int(input())
coin=list(map(int,input().split()))
coin.sort()
target=1
for i in range(n):
    if target<coin[i]:
        break
    target+=coin[i]
    
print(target)

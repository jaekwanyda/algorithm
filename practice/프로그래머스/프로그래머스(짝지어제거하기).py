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

#https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    #일일이 하는 것은 시간복잡도 문제 발생=>stack을 이용해서 100만개를 한꺼번에 체크
    stack=[];cnt=0 #시작 index는 0부터
    if len(s)%2!=0:#list가 홀수인 경우 어차피 실패
        return 0
    while cnt<len(s):
        k=s[cnt]
        if cnt<len(s)-1 and k==s[cnt+1]: #만약 다음 문자와 같으면 한칸 점프
            cnt+=2
        else: #아닌 경우 stack과도 비교
            if stack and stack[-1]==k:
                stack.pop()
            else:
                stack+=k
            cnt+=1
    if len(stack)==0:
        answer=1
    else:
        answer=0
        
    return answer

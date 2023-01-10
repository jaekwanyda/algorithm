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
#이코테 실전 18(프로그래머 60058)
p=')())()()())))))(((()()(()(())))))'

def balance(p): #균형잡힌 괄호 문자열 출력해주는 함수
    #가능한 첫 균형잡힌 골호 문자열을 u로 만들기
    left=0 #왼쪽 괄호 수
    right=0 #오른쪽 괄호 수
    u_index=0
    for i in range(len(p)):     
        if p[i]=='(':
            left+=1
        else:
            right+=1
        u_index+=1
        if left==right:
            break
    u=p[:u_index] #u 생성
    v=p[u_index:] #v 생성
    return (u,v)
def correct(p): #올바른 괄호 문자열인지 확인하는 함수
    left=0
    right=0
    for i in range(len(p)):
        if p[i]=='(':
            left+=1
        else:
            right+=1
        if left<right:
            return False
    return True
def solution(p):
    answer = ''
    if p=='':
        return answer
    u,v=balance(p)[0],balance(p)[1]
    if correct(u):
        answer=u+solution(v)
    else:
        answer='('
        answer+=solution(v)
        answer+=')'
        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i]=="(":
                answer+=')'
            else:
                answer+='('
    return answer
print(solution(p))
# -





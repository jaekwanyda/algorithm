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

def solution(m, musicinfos):
    answer = '(None)'
    result=[[0,'',''] for _ in range(len(musicinfos))]
    for i,k in enumerate(musicinfos):
        m_list=list(k.split(','))
        result[i][0]=int(m_list[1][:2])*60+int(m_list[1][3:])-(int(m_list[0][:2])*60+int(m_list[0][3:]))#재생 시간
        result[i][1]=m_list[2]
        result[i][2]=str((result[i][0]//len(m_list[3])+10000)*m_list[3])[:result[i][0]+777]
    result=sorted(result,key=lambda x:-x[0])
    for r in result:
        if m in r[2]:
            a=list(r[2].split(m));possi=False
            for i,j in enumerate(a):
                if i>0:
                    if len(j)==0:
                        if i==len(a)-1:
                            possi=True
                        elif len(a[i+1])==0:
                            possi=True
                    else:
                        if j[0]!='#':
                            possi=True
            if possi:
                return r[1]
    
    return answer


print('12:00')



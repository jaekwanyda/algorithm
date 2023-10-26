import sys
input = sys.stdin.readline
#아이디어: 정규표현식 사용
import re
m = re.compile(r'-?\d+')
answer = []
n = re.compile(r'-?\d*x*')
poli = n.findall(input().rstrip())
for i,p in enumerate(poli):
    if p =='':
        continue
    parameter = m.findall(p)
    if not parameter:
        parameter = 1
    else:
        parameter = int(parameter[0])
    parameter /= p.count('x')+1
    p = re.sub(m,'',p)
    if parameter == 1:
        p += 'x'
    elif parameter == -1:
        p = '-' + p + 'x'
    else:
        p = str(int(parameter)) + p + 'x'
    if p[0] != '-' and i>0:
        p = '+' + p
    if int(parameter) == 0:
        poli.pop(i)
    else:
        poli[i] = p
if all(p=='' for p in poli):
    print('W')
else:
    print(''.join(poli)+'+W')
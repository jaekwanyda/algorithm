import sys
input = sys.stdin.readline

k = input().strip()

possi_c = True
possi_java = True

if k[0] == '_' or k[-1] == '_' or '__' in k:
    possi_c = False
else:
    for i in range(len(k)):
        if k[i] == '_' and k[i + 1] == '_':
            possi_c = False
        elif k[i] != '_' and k[i] == str.upper(k[i]):
            possi_c = False

if k[0] == k[0].upper() or '_' in k:
    possi_java = False

if possi_c:
    k = list(k)
    i = 0
    while i < len(k):
        if k[i] == '_':
            k.pop(i)
            k[i] = k[i].upper()
        i += 1

if possi_java:
    k = list(k)
    i = 0
    while i < len(k):
        if k[i] == k[i].upper():
            k[i] = '_' + k[i].lower()
        i += 1

if all(i == i.lower() and i != i.upper() for i in k):
    print(''.join(k))
elif not (possi_java or possi_c) or (possi_java and possi_c):
    print("Error!")
else:
    print(''.join(k))

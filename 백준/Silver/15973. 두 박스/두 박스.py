import sys
input = sys.stdin.readline

ax1, ay1, ax2, ay2 = map(int, input().split())
list_a = [(ax1, ay1), (ax1, ay2), (ax2, ay1), (ax2, ay2)]

bx1, by1, bx2, by2 = map(int, input().split())
list_b = [(bx1, by1), (bx1, by2), (bx2, by1), (bx2, by2)]

# Nullity investigation
null_possi = False
if bx2 < ax1 or bx1 > ax2 or by2 < ay1 or by1 > ay2:
    null_possi = True
if null_possi:
    print('NULL')
elif (ax1,ay1)==(bx2,by2) or (ax2,ay1)==(bx1,by2) or (ax1,ay2)==(bx2,by1) or (ax2,ay2)==(bx1,by1):
    print('POINT')
elif ax1==bx2 or ax2==bx1 or ay1==by2 or ay2==by1:
    print("LINE")
else:
    print('FACE')

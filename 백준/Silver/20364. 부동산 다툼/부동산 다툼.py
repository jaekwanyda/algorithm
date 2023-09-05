import sys
input = sys.stdin.readline
#아이디어: 부모노드를 차례차례 확인 가능하면 O(Q)정도면 확인할 수 있다.
#n,q 입력받기
n,q = map(int,input().split())
#오리가 원하는 땅 입력받기
visit_dict = {}
for _ in range(q):
    want = int(input())
    original = want
    possi = True
    while want:
        if want in visit_dict:
            possi = False
            break_point = want
        #부모 노드 확인하기
        want = want//2
    
    if possi:
        visit_dict[original] = True
        print(0)
    else:
        print(break_point)
    
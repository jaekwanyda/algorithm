import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
#아이디어: 
# 50 30 24 5 28 45 98 52 60 #node 보다 큰 첫 수가 right node, 바로 뒤가 left node
# 5 28 24 45 30 60 52 98 50 
class tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def dfs(preorder):
    if not preorder:
        return None
    result_tree = tree(preorder[0])
    cut = len(preorder)
    for i in range(len(preorder)):
        if preorder[i] > preorder[0]: #node 보다 큰게 나오는 순간 right node 시작
            cut = i
            break
    #right node가 존재하면
    if cut < len(preorder):
        result_tree.left = dfs(preorder[1:cut])
        result_tree.right = dfs(preorder[cut:])
    else:
        #left node가 존재하면
        if len(preorder) > 1:
            result_tree.left = dfs(preorder[1:])
    return result_tree
preorder = []
while True:
    a = input()
    if a != '':
        preorder.append(int(a))
    else:
        break
postorder = [] #왼->오->루
answer = dfs(preorder)
node = answer
def dfs2(tree):
    if tree and tree.left == None and tree.right == None: #리프 노드 인 경우
        postorder.append(tree.val)
        return
    if tree:
        dfs2(tree.left)
        dfs2(tree.right)
        postorder.append(tree.val)
dfs2(answer)
for p in postorder:
    print(p) 
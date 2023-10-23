import sys
input = sys.stdin.readline
#아이디어: 총 10개의 set를 만들어 n자리 숫자가 들어오면 1~n 자리 까지 set에 다 넣어주고 숫자를 세자
t = int(input())
for _ in range(t):
    n = int(input())
    array = []
    len_list = set()
    for _ in range(n):
        a = input().rstrip()
        array.append(a)
        len_list.add(len(a))
    len_list = sorted(list(len_list))
    array = sorted(array,key = lambda x:len(x))
    #나온 길이만 체크해주기
    def check(array):
        set_list = [set() for _ in range(11)]
        for a in array:
            for l in len_list:
                if l > len(a):
                    break
                if a[:l] in set_list[l]:
                    print('NO')
                    return
                elif l == len(a):
                    set_list[l].add(a[:l])
        print('YES')
        return
    check(array)
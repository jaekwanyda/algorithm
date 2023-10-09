import sys
input = sys.stdin.readline
#아이디어: 혼자 받을 수 있는 책은 그 학생이 => 만약 여럿이면? 범위가 좁은 애부터
#t입력받기
t = int(input())
for _ in range(t):
    #n,m 입력받기
    n,m = map(int,input().split())
    array = [0]*(n+1) #책을 줬는지 저장하는 리스트
    books = []
    for _ in range(m):
        books.append(list(map(int,input().split())))
    books = sorted(books,key = lambda x: x[1]) #b를 기준으로 오름차순 정렬
    answer = 0
    for book in books:
        for i in range(book[0],book[1]+1):
            if array[i] == 0:
                array[i] = 1
                answer += 1
                break
    print(answer)
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
#이코테 실전 23(백준 10825)
#아이디어: 국어-> 영어 -> 수학-> 이름 순 정렬(정렬라이브러리 이용! 방법 잘 몰라서 참고해서 함!!)

#n입력받기
n=int(input())
#학생 정보 입력받기
student=[list(input().split()) for _ in range(n)]
#key뜻: 국어성적 내림, 영어 오름, 수학 내림, 이름 오름 순=> 의문 사전 대문자, 소문자는 처리 안해줘도 되나?(key구문 사용법 숙지!)
student.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in student:
    print(i[0]) #이름 출력 

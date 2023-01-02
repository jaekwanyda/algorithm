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

#이코테 구현 예제 2
#나이트의 위치 입력받기
input_data=input()
data_row=int(input_data[1]) # 입력 받은 것은 str!
data_column=int(ord(input_data[0]))-int(ord('a'))+1 # ord 를 사용해서 순서 확인하기!(몰랐던 것)
steps=[[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
result=0
for step in steps:
    next_row=data_row+step[0]
    next_column=data_column+step[1]
    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8:
        result+=1
print(result)



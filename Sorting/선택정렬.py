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
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    #i 번째 부터 선택 시작
    min_id=i
    for j in range(i+1,len(array)):
        if array[min_id]>array[j]:
            min_id=j
    array[i],array[min_id]=array[min_id],array[i]
print(array)
# -



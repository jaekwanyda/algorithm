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
from itertools import combinations #tool의 중요성!!
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        print(counter)
        if len(counter) != 0 and max(counter.values()) != 1:
            for f in counter:
                if counter[f]==max(counter.values()):
                    answer+=[''.join(f)]
    answer.sort()
    return answer

def solution(name, yearning, photo):
    answer = []
    year_dict = {n:y for n,y in zip(name,yearning)}
    for pho in photo:
        ans = 0
        for p in pho:
            if p in year_dict:
                ans += year_dict[p]
        answer.append(ans)
    return answer
def solution(a):
    answer = 0
    left = [0]*(len(a))
    right = [0]*(len(a))
    left[0] = a[0]
    right[-1] = a[-1]
    for i in range(1,len(a)):
        left[i] = min(left[i-1],a[i])
        right[-i-1] = min(right[-i],a[-i-1])
    for i in range(len(a)):
        if i == 0 or i == len(a)-1:
            answer += 1
        else:
            if not(a[i] > left[i-1] and a[i] > right[i+1]):
                answer += 1
            
    return answer
def solution(survey, choices):
    answer = ''
    result_dict = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    length = len(survey)
    for i in range(length):
        negative_target = survey[i][0]
        positive_target = survey[i][1]
        score = choices[i]
        if score<4: #negative
            result_dict[negative_target] += 4-score
        elif score>4: #positive
            result_dict[positive_target] += score-4
    #R,T 구분
    if result_dict['R'] >= result_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    #C,F 구분
    if result_dict['C'] >= result_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    #J,M 구분
    if result_dict['J'] >= result_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    #A,N 구분
    if result_dict['A'] >= result_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer
def solution(players, callings):
    player_to_index = {player:idx for idx,player in enumerate(players)}
    idx_to_player = {idx:player for idx,player in enumerate(players)}
    for calling in callings:
        change_idx = player_to_index[calling]
        #추월하면 index -1
        player_to_index[calling] -= 1
        #추월 당한 놈 찾기
        idx_to_player[change_idx-1],idx_to_player[change_idx] = idx_to_player[change_idx],idx_to_player[change_idx-1]
        player_to_index[idx_to_player[change_idx]] += 1
    answer = [x for x,_ in sorted(player_to_index.items(),key = lambda x:x[1])]
    return answer
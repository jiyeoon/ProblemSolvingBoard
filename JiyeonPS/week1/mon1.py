# 프로그래머스 섬 연결하기

# n : 섬의 개수 / cost : 두 섬을 연결하는 번호 & 다리를 건설할때 드는 비용이 들어있다.
def solution(n, costs):
    answer = 0
    ch = [0 for _ in range(n)] # 체크 배열. 해당 섬을 방문하면 1로 체크
    
    costs.sort(key=lambda x: x[2]) # 비용 순서대로 sort
    
    #print(costs)
    
    ch[0] = 1 # 0부터 시작한다 (?)
    while 0 in ch:
        for cost in costs:
            _from, _to = cost[0], cost[1]
        
            if ch[_from] == 1 or ch[_to] == 1: # 둘중 하나가 1이면 연결되어있다는 뜻이니까
                if ch[_from] == 1 and ch[_to] == 1: # 둘다 1이면 넘어감
                    pass
                else:
                    ch[_from], ch[_to] = 1, 1 # 둘다 1로 체크하고 비용을 더해주고 넘어감
                    answer += cost[2]
                    break
            #print("from : {}, to : {}, cost : {}".format(_from, _to, cost[2]))
            #print("answer : {}, ch : {}".format(answer, ch))
        
    return answer
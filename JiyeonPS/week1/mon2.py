"""
LeetCode 330 문제

기본 로직 
1. 1부터 n/2 까지의 수를 rem 
2. res가 return 값. res 수만큼 rem 배열에서 pick 한 다음 nums 배열을 새로 만듦
3. 새로 만든 new_nums 배열에서 모든 조합의 합을 구한다. ch 배열에 sum 번째에의 값을 1로 설정
4. ch 배열에서 0이 없으면 flag를 1로 바꾸고 break. 없으면 계속 반복.
5. 한번 res가 끝나면 계속 더하면서 gogogo

==> Time Out Error가 난다.
"""

from itertools import combinations
import math

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ch = [0 for _ in range(n+1)]
        rem = []
        for i in range(1, math.ceil(n/2 + 1)):
            if i not in nums:
                rem.append(i)
                
        res = 0
        #print(rem)
        
        # 배열 아무것도 쓰지 않을 때 초기값 검사
        for i in range(1, len(nums)+1):
            for one_comb in list(combinations(nums, i)):
                s = sum(one_comb)
                ch[s-1] = 1
        
        if 0 not in ch[1:]:
            return res
        else:
            res = res +1
        
        
        while True:
            flag = 0
            
            # res 수만큼 rem 배열에서 pick해서 nums 배열 다시 만듦
            
            for one_list in list(combinations(rem, res)):
                new_num = nums[:] + list(one_list)
                #print("new_num : ", new_num)
                
                for j in range(1, len(new_num)+1): # 모든 조합들의 sum을 구함. 구한 sum은 ch 배열에서 더해준다.
                    for one_comb in list(combinations(new_num, j)):
                        
                        s = sum(one_comb)
                        #print("s : ", s, ", one_comb : ", one_comb)
                        if s > n:
                            continue
                        else:
                            ch[s] = 1
                
                if 0 not in ch[1:]:
                    flag = 1
                    break
                else:
                    ch = [0 for _ in range(n+1)] # ch 배열 초기화
                    continue
            
            # 다시 만든 nums 배열에서 모든 조합들의 sum을 구함. ch 배열에서 sum을 빼줌.
            
            # ch 배열에서 0이 없으면 flag = 1로 바꿈. 없으면 flag = 0으로 res값을 더해줌. 
            
            
            if flag == 1:
                break
            else:
                res = res + 1
        
        
        return res
        
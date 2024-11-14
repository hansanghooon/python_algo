# 이진 탐색 이용해서 문제 해결
# bin_search 에 자세한 설명

import math 
def pass_level_time(diffs,times,limit,level):
    
    total_time=0
    bef_time=0
    for diff,time in zip(diffs,times):
        if level < diff :
            need_iter= (diff-level)
            total_time= total_time+((bef_time+time)*need_iter)+time
        else:
            total_time=total_time+time
            
        bef_time=time
        
    print(total_time)
    res=True
    if limit < total_time:
        res=False
        
    return res


#  최소레벨을 low_level 최대 레벨을 high_level 이라 하면 통과가 가능한 최소 레벨은 저 두 숫자 사이임
#  결과를 만족하는 레벨을 low_level +a 로 찾음, a값을 이진으로 표현해 이진 탐색을 진행
# 최소와 최대 레벨의 차이가 2**n 보다 작거나 같을 경우, 2**(n-1) 부터 시작해서 1까지 low_level 에 더해가며(cur_lvel에 누적합) 최소가 되는 level 찾을것임
# 마지막에 테스트 하여 1을 더하는 이유는  low_level+a 에서 a가 2**n일 경우 누적합을 이용한 조건에서 만족하지 않는 부분   발견해서 수정
def bin_search(low_level,high_level,diffs,times,limit):
    
    differecne=high_level-low_level
    
    pow_2=2**int(math.log2(differecne))
    
    cur_level=low_level
    

    while pow_2:
        
        decision_add=1-int(pass_level_time(diffs,times,limit,cur_level+pow_2))
        cur_level=cur_level+decision_add*pow_2
        pow_2=pow_2//2
    
    if 1-int(pass_level_time(diffs,times,limit,cur_level)):
        cur_level=cur_level+1
    
    
    return cur_level


def solution(diffs, times, limit):
    
    
    levels_orderd=diffs.copy()
    levels_orderd.sort()
    
    # bef_level=0
    # for level in levels_orderd:
    #     if pass_level_time(diffs,times,limit,level):
    #         cur_level=level
    #         break        
    #     bef_level=level
    
    answer=bin_search(1,max(diffs),diffs,times,limit)

    
    return answer
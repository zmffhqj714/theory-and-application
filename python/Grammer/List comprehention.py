#사용하는 이유
map, lambda , filter 같은 함수형을 기능이 있지만 
기존 리스트를 기반으로 새로운 리스트를 만들어 낼 때 가독성이 좋아 사용한다.

#  코드 
 # map , lambda
    print(list(map(lambda x : x +1 , (1,2,3) )))
# List comprehention
    print([y +1 for y in range(1, 4)]

같은 코드 이지만 좀 더 직관적으로 볼 수 있다.

from collections import defaultdict
def solution(sizes):
    
 # map , lambda
    print(list(map(lambda x : x +1 , (1,2,3) )))
# List comprehention (list 안에서 바로 구현을 하여 바로 사용할 수 있음, 
# 너무 많이 표현식을 주게되면 복잡하므로 )
    print(sizes)
    print(sizes[1])
    # 홀수인 경우 볼 수 있음
    print([  i  for i in range(1,10) if i % 2 ==1])
    # 딕셔너리형1
    print({i for i in range(1,10) if i %2  == 0})
    
    # 딕셔너리형2 (int, list, set 전부가능 )
    
    a = defaultdict(list) #simmiar dict
    for i in range(1,5):
        a[i].append(i)
   
  
    d = {key: value for key , value in a.items()}

    print(a) # 이렇게 출력하면 class 형으로 나옴 
    print(d) # 진정한 dic형식의 list 가 나옴

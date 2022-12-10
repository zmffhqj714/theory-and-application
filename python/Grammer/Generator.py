import sys
import timeit  
def solution(sizes):
    # 제너레이터 : 메모리를 사용하지 않고 임의의 숫자를 만들어서 사용이 가능하다.
    def get_number ():
        n = 0
        while True :
            n += 1
            if n %2 ==0:
                yield n # 계속 리턴 가능
                yield '될까?'
                yield list([1,2,3])
                yield True
    gn = get_number()
    
    for _ in range(0,10):
        #만든 gnerate값을 생성하여 return 
        print(next(gn))

 #gernarate를 사용해야 하는 이유 ex)  range
# 실제값을 생성해야함 1,1억개여도 대기하는 메모리의 양은 같음 , 필요한 수만 메모리에 올려줄 수 있다
    a = range(1000000)
# 사용예시
    b = [i for i in range(1000000)]
    c = (i for i in range(1000000))
    # 타입비교
    print(type(a))
    print(type(b))
    
    #메모리비교
    print(sys.getsizeof(b)) # 8697456 메모리 차지
    print(sys.getsizeof(c)) #112 메모리 차지
  
# 결론 : 표현식이 다양하지 않다면 List의 apperehention 방식을 Grarate형으로 변경하여 사용하도록 한다.
    return 1

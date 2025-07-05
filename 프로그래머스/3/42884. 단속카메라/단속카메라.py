def solution(routes):
    routes.sort(key = lambda x: x[1])
    camera = routes[0][1]
    cnt = 1
    
    for route in routes[1:]:
        if route[0] > camera:
            cnt += 1
            camera = route[1]
            
    return cnt
'''
-20 ~ -15 사이 카메라 없으니 -15에 설치
-18 ~ -13 사이에 카메라 있으니 설치 X 
-> '카메라가 있다' => 이 전 루트의 마지막보다 첫번째 숫자가 작다 
-14 ~ -5 사이에 카메라 없으니 -5에 설치
-5 ~ -3 사이에 카메라 있으니 설치 X 
=> 2개 return
'''
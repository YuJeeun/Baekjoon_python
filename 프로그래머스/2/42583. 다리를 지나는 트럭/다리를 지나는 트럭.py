from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    total = 0
    trucks = deque(truck_weights)
    
    while bridge:
        answer += 1
        dest = bridge.popleft()
        total -= dest
        
        if trucks:
            if total + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                total += truck
            else:
                bridge.append(0)
                
    return answer









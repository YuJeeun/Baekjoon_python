from collections import Counter

word = input().strip().upper() 
counter = Counter(word)  
max_count = max(counter.values()) 

most_common = [char for char, count in counter.items() if count == max_count]

print("?") if len(most_common) > 1 else print(most_common[0])

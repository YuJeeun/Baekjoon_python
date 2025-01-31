s = input()
positions = [-1] * 26
for i, char in enumerate(s):
    index = ord(char) - ord('a')
    if positions[index] == -1:
        positions[index] = i
        
print(" ".join(map(str, positions)))

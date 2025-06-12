def solution(files):    
    answer = []
    heads, numbers, tails = files_split(files)
    parsed_files = []
    for i in range(len(files)): 
        parsed_files.append((files[i], heads[i], numbers[i], tails[i], i))
    
    parsed_files.sort(key = lambda x: (x[1].upper(), int(x[2]), x[4]))
    
    sorted_files = []
    for i in range(len(parsed_files)): sorted_files.append(parsed_files[i][0])
    
    return sorted_files
    
def files_split(files):
    heads, numbers, tails = ['']*len(files), ['']*len(files), ['']*len(files)
    idx = 0
    for i in range(len(files)):
        for j in range(len(files[i])):
            if files[i][j].isnumeric(): 
                idx = j
                break
            heads[i] += files[i][j]
        
        for j in range(idx, len(files[i])):
            if not files[i][j].isnumeric():
                idx = j
                break
            numbers[i] += files[i][j]
        
        for j in range(idx, len(files[i])):
            tails[i] += files[i][j]
    
    return heads, numbers, tails
    
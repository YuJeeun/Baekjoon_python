def solution(skill, skill_trees):
    sstr = ''
    cnt = 0
    for skill_tree in skill_trees:
        sstr = ''
        for s in skill_tree:
            if s in skill:
                sstr += s
                
        if skill.startswith(sstr): 
            cnt += 1
            
    return cnt
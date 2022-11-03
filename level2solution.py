def solution(s):
    removed_dash=s.replace("-","")
    salutes=0
    for i,direction in enumerate(removed_dash):
        if direction == '>':
            front_soldiers=removed_dash[i:]
            left_soldiers=front_soldiers.count('<')
            salutes += left_soldiers *2
    return salutes

def max_consecutive_difference(lst):
    if len(lst) < 2:
        return 0
    
    res = 0
    for i in range(len(lst) - 1):
        diff = lst[i] - lst[i + 1]
        if diff < 0:
            diff = -diff
        if diff > res:
            res = diff
            
    return res
    

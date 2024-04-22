def mostCommonName(L):
    if not L:
        return None
    
    count = {}
    max_count = 0
    most_common_names = set()
    
    for name in L:
        count[name] = count.get(name, 0) + 1
        
        if count[name] > max_count:
            max_count = count[name]
            most_common_names = {name}
        elif count[name] == max_count:
            most_common_names.add(name)
    
    if most_common_names:
        return most_common_names
    else:
        return None

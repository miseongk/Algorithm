import itertools

def solution(user_id, banned_id):
    result = set()
    possible_list = list(itertools.permutations(user_id, len(banned_id)))
    
    for p in possible_list:
        users = check(p, banned_id)
        if len(users) == len(banned_id):
            result.add(tuple(users))
            
    return len(result)
    
    
def check(p, banned_id):
    users = []
    
    for p_id, b_id in zip(p, banned_id):
        if len(p_id) != len(b_id):
            return []
        for idx, c in enumerate(b_id):
            if c == "*":
                continue
            if c != p_id[idx]:
                return []
        users.append(p_id)
            
    return sorted(users)

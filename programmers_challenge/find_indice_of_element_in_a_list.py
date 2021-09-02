# for a given list L, find index of element x and return a list of indices
# if x not in L, return [-1]

def solution(L, x):
    indices = []
    if x not in L:
        indices.append(-1)
    
    for i, n in enumerate(L):
        if n == x:
            indices.append(i)

    return indices


L1 = [64, 72, 83, 72, 54]
x1 = 72

L2 = [64, 72, 83, 72, 54]
x2 = 83

L3 = [64, 72, 83, 72, 54]
x3 = 99

print(solution(L1, x1))
print(solution(L2, x2))
print(solution(L3, x3))

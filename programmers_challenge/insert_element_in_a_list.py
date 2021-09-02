# for a given sorted list L, insert x in L such that the final output is still sorted
# i.e. L = [20, 37, 58, 72, 91]
# x = 66
# output = [20, 37, 58, 66, 72, 91]

def solution(L, x):
    count = 0

    for i in range(len(L)):
        if L[i] < x:
            count += 1
    L.insert(count, x)

    return L


L = [20, 37, 58, 72, 91] 
x = 66

print(solution(L, x))

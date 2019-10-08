def findMinAndMax(L):
    if L == []:
        return (None, None)
    if len(L) == 1:
        return (L[0], L[0])
    else:
        return (max(L), min(L))

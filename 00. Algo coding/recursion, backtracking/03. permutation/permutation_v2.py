"""
        nums = [1,2,3]
        taken = {1:F, 2:F, 3:F}
        result = [[1,2,3]]
        li = []

        [] -> [1], {1:T, 2:F, 3:F}
        [1] -> [1,2], {1:T, 2:T, 3:F}
        [1,2] -> [1,2,3], {1:T, 2:F, 3:T} 
        [1,2,3] <- None {1:T, 2:F, 3:F}
        [1,2] <- None {1:T, 2:F, 3:F}
        [1] -> [1, 3] {1:T, 2:F, 3:T}
        [1, 3] -> [1,3,2] {1:T, 2:T, 3:T}
        [1,3,2] <- None {1 : T, 2 : F, 3:T}
        [1, 3] <- None {1 : T, 2: F, 3 : F}
        [1] <- None {1 : F, 2 : F, 3 : F}

        [] -> [2] {1: F, 2:T, 3:F}
        [2] -> [2, 3] {1:F, 2:T, 3:T}
        [2,3] -> [2,3,1] {1: T, 2:T, 3:T}
        [2,3,1] <- None {1:F, 2:T, 3:T}
        [2, 3] <- None {1:F, 2: T, 3: F}
        [2] -> [2, 1] {1:T, 2:T, 3:F}
        [2,1] -> [2,1,3] {1:T, 2:T, 3:T}
        [2,1,3] <- None {1:T, 2:t, 3: f}
        [2,1] <- None {1:F, 2:T, 3:F}
        [2] <- None {1:F, 2:F, 3:F}
        [] <- None {1:F, 2:F, 3:F}

        [] -> [3] {1:F, 2:F, 3:T}
        ....
"""

from collections import defaultdict


def getPermutations(array):
    if array == []:
        return array
    result = []
    seen = defaultdict(bool)
    permutationsHelper(array, [], seen, result)
    return result


def permutationsHelper(array, li, seen, result):
    if len(array) == len(li):
        result.append(li.copy())
        return None
    for item in array:
        if seen[item]:
            continue
        seen[item] = True
        permutationsHelper(array, li + [item], seen, result)
        seen[item] = False
    return None


print(getPermutations([1, 2, 3]))

""" 
                 [1,2,3], []
              /        |      \
    
      [2,3], [1]    [1,3], [2]    [1,2], [3]
    /         \
[2],[1,3]   [3],[1,2]
    |             
[],[1,3,2]   
"""


def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations


def permutationsHelper(arr, permutation, permutations):
    if len(arr) == 0 and len(permutation):
        permutations.append(permutation)
        return
    for i in range(len(arr)):
        newArr = arr[:i] + arr[i+1:]
        newPermutation = permutation + [arr[i]]
        permutationsHelper(newArr, newPermutation, permutations)

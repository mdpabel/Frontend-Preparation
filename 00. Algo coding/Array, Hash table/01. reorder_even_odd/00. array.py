li = [1, 2, 3, 4, 5]

""" 1, 2, 3, 4, 5
0, 4 -> 1, 2, 3, 4, 5
0, 3 -> 5, 2, 3, 4, 1
0, 2 -> 4, 2, 3, 5, 1
1, 2 -> 4, 2, 3, 5, 1
2, 2 -> 4, 2, 3, 5, 1
"""


def even_odd(li):
    next_even, next_odd = 0, len(li) - 1

    while next_even < next_odd:
        if li[next_even] % 2 == 0:
            next_even += 1
        else:
            li[next_even], li[next_odd] = li[next_odd], li[next_even]
            next_odd -= 1


even_odd(li)

print(li)

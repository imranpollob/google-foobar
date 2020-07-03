from itertools import combinations


def solution(l):
    l.sort(reverse=True)
    for i in reversed(range(1, len(l) + 1)):
        for tup in combinations(l, i):
            if sum(tup) % 3 == 0:
                print(int(''.join(map(str, tup))))
                return
    print(0)


solution([3, 1, 4, 1])
solution([3, 1, 4, 1, 5, 9])
solution([3, 1, 4, 1, 0, 1])
solution([0, 1])


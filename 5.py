def solution(l):
    cnt = 0
    memo = [0] * len(l)
    print('memo- ',memo)
    for i in xrange(len(l) - 1):
        for j in xrange(i + 1, len(l)):
            print(l[j] , l[i])
            if l[j] % l[i] == 0:
                memo[j] += 1
                cnt += memo[i]
                print(l[j] % l[i])
                print('memo ----->> ', memo, )
    return cnt
# print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))

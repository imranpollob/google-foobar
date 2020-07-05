def with_add(num):
    steps = 0

    while num > 1:
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num += 1

        steps += 1

    return steps


def with_sub(num):
    steps = 0

    while num > 1:
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num -= 1

        steps += 1

    return steps


def solution(num):
    num = int(num)

    return min(with_add(num), with_sub(num))


print(solution(15))
print(solution(4))

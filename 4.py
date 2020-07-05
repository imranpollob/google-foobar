def solution(num):
    num = int(num)
    count = 0

    while(num > 1):
        if (num & 1 == 0):
            # Dividing even number by two by shifting binary digits one step to the right.
            num = num >> 1
        else:
            a = num + 1
            b = num - 1
            # counters ac & bc will be used to count trailing 0s
            ac = bc = 0
            # count trailing 0's for num+1
            while(a & 1 == 0):
                a = a >> 1
                ac += 1

            print(num, 'ac', ac)

            # count trailing 0's for num-1
            while(b & 1 == 0):
                b = b >> 1
                bc += 1

            print(num, 'bc', bc)

            # go with num+1 if it has more trailing 0s in binary format. Exception is number 3 as b10 can be divided in less steps than b100.
            # edge case 3 identified by manually testing numbers 1-10.
            if (ac > bc and num != 3):
                num += 1
            else:
                num -= 1
        count += 1

    return count


print('Solution - ', solution(15))
print('-----')
print('Solution - ', solution(100))
print('-----')
print('Solution - ', solution(4))
print('-----')
print('Solution - ', solution(3))
print('-----')
print('Solution - ', solution(2))
print('-----')
print('Solution - ', solution(1))
print('-----')
print('Solution - ', solution(0))

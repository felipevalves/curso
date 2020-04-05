from symbol import test


def solution(number):
    numbers = [i for i in range(1, number) if i % 3 == 0 or i % 5 == 0]
    return sum(numbers)

# print(solution(10))


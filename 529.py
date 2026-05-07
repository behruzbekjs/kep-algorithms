def divisors_count(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count


def map_divisors_count(numbers):
    return list(map(divisors_count, numbers))
import sympy


def prime_digit_sum_matches_position(n):

    primes = []
    position = 1
    candidate = 2

    while len(primes) < n:
        if sympy.isprime(candidate):
            prime_digit_sum = sum(int(d) for d in str(candidate))
            position_digit_sum = sum(int(d) for d in str(position))

            if prime_digit_sum == position_digit_sum:
                primes.append(candidate)

            position += 1
        candidate += 1

    return sum(primes)


result = prime_digit_sum_matches_position(10000)
result

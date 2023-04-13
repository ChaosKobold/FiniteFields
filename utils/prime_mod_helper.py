

def is_prime(p: int) -> bool:
    """
    Checks whether a given int is a prime number.
    :param p:
    :return:
    """
    if p < 2:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
        if i*i > p:
            return True
    return True

def get_inverse_entries(prime: int):
    inverses: list[int] = [0] * prime
    for i in range(1, prime):
        if i == 0:
            continue
        for j in range(1, prime):
            if (i * j) % prime == 1:
                inverses[i] = j
                break
    return inverses

def get_first_primes(n: int) -> list[int]:
    if n <= 0:
        return []
    result = []
    i = 0
    while len(result) < n:
        if is_prime(i):
            result.append(i)
        i += 1
    return result



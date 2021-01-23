from random import randint
from math import gcd

def is_prime(n):
    if n < 2: return False
    for p in range(2, n):
        if n % p == 0:
            return False
    return True


def lcm(a, b):
    n = a*b / gcd(a, b)
    return int(n)


def main():
    p = q = 0
    while not is_prime(p):
        p = randint(2,100)
    while not is_prime(q):
        q = randint(2,100)
    N = p * q
    L = lcm(p-1, q-1)
    E = 2
    while gcd(E, L) != 1:
        E += 1 #TODO: randomにする
    D = 1
    while E*D % L != 1:
        D += 1

    print(f'N: {N}\nE: {E}\nD: {D}')


if __name__ == "__main__":
    main()
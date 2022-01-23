f = open('input.txt', 'r')

def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int, int]:
    # ax + by = gcd(a, b)
    # return (x, y, gcd(a, b))
    r0 = max(a, b)
    r1 = min(a, b)
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r2 = r0 % r1
        s2 = s0 - q*s1
        t2 = t0 - q*t1
        r0, r1 = r1, r2
        s0, s1 = s1, s2
        t0, t1 = t1, t2
    x = s0
    y = t0
    if a < b:
        x, y = y, x
    return x, y, r0



def chinese_remainder_theorem_2(a1: int, a2: int, n1: int, n2: int) -> int:
    # x % n1 = a1
    # x % n2 = a2
    # return smallest such x
    m1, m2, _ = extended_euclidean_algorithm(n1, n2)
    x = a1 * m2 * n2 + a2 * m1 * n1
    return x

f.readline()
buses: list[tuple[int, int]] = [(int(num), i) for i, num in enumerate(f.readline().split(',')) if num!='x']
buses = [(num, (num-(rem%num))%num) for num, rem in buses]
while len(buses) > 1:
    n1, a1 = buses[0]
    n2, a2 = buses[1]
    x = chinese_remainder_theorem_2(a1, a2, n1, n2)
    a12 = x % (n1*n2)
    buses = [(n1 * n2, a12)] + buses[2:]
print(buses)

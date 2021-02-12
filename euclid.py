def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# cases = [
#     (12,6,6), (13,3,1), (14,6,2), (13,6,2)
# ]

# for a,b,c in cases:
#     assert c == gcd(a,b)


def inverse(n, a):
    x_0, y_0, x_1, y_1 = 1, 0, 0, 1
    while a != 0:
        n, a, q = a, n % a, n // a
        x_0, y_0, x_1, y_1 = x_1, y_1, x_0 - q*x_1, y_0 - q*y_1
    return y_0


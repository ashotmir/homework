def gcd(*args):
    if len(args) < 2:
        return None
    if len(args) == 2:
        a, b = args
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    else:
        return gcd(args[0], gcd(*args[1:]))


gcd(12, 24, 26)

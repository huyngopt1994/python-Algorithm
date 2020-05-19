def fast_power(a, n):
    if n == 1:
        return a
    else:
        x = fast_power(a, n // 2)
        if not (n % 2):
            # even
            return x * x
        else:
            return x * x * a


print(fast_power(4, 4))

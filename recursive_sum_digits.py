def sum_digits(n):
    if n < 1:
        return 0

    digit = n % 10
    n = int(n / 10)
    return digit + sum_digits(n)


if __name__ == '__main__':
    print(sum_digits(43219))

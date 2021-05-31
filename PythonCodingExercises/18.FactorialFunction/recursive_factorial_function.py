def factorial(n: int) -> int:
    """
    Return n! (0! is 1).

    Valid for `n` in the range of 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursiveError.
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)

for i in range(36):
    print(i, factorial(i))
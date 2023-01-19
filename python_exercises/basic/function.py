def sum(a, b):  # definition name(arguments)
    return a + b  # return value and stop execution of functoin code


s = sum(1, 2)  # calling


def power(x, y=2):  # definition with default value for arguments
    return x ** y


def cumulative_sum(start: float, end: float, gap: float = 1) -> float:  # definition with tipy checks
    if start == end:
        return end
    return start + cumulative_sum(start + gap, end, gap)  # function can call itself


print(cumulative_sum(1, 100))

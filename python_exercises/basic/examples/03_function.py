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

# il nome di una fuzione è un puntatore alla stessa
a = sum
b = power
print(a(7, 2))
print(b(7, 2))


# utile per usare e creare funzioni generiche
def k(x):
    return (x % 3) + (x / 10)  # definizione di una strana comparazione


list = [11, 2, 6, 18, 9, 17]

print(sorted(list))
print(sorted(list, key=k))

# si posso anche definire funzioni anonime come lambda

list = ["az", "jjj", "12", "obc", "obd"]

print(sorted(list, key=lambda x: x[::-1]))  # string reversing [start_index:stop_index:step]

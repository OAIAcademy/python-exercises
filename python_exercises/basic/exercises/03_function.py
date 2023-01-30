# 1 - create a function which check if a string is a palindrome,
#               returning a bool and the list of tuple of not matching letters
#               (es f("aabca") -> False , [('a','c')])
# 2 - create a function to remove a list of key from a dict and return the keys not found as a list
# 3 - create a recursive function that compute nth the fibonacci numbers (f(n) = f(n-1) + f(n-2), f(1) = 1 ,f(2) = 1)































# SOLUTIONS
# 1
def palindrome(s: str):
    ret = []
    for i in range(0, int(len(s) / 2)):  # no need to check two times the same letters or the middle letter
        if s[i] != s[-i - 1]:
            ret.append((s[i], s[-i - 1]))
    return len(ret) == 0, ret


print(palindrome("aabca"))


# 2
def rem_from_dict(d: dict, l: list) -> []:
    ret = []
    for k in l:
        if k in d:
            d.pop(k)
        else:
            ret.append(k)
    return ret


print(rem_from_dict({"a": 1}, ["a", "B"]))


# 3
def fibonacci(n: int) -> int:
    if n in [1, 2]:  # fixed/termination case
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)  # recursie call


def faster_fibonacci(n: int, m=None) -> int:  # using a list to not redo done calculation
    if m is None:  # init the memory dict
        m = {}

    if n in [1, 2]:  # fixed/termination case
        return 1

    if n - 2 not in m:
        m[n - 2] = faster_fibonacci(n - 2, m)

    if n - 1 not in m:
        m[n - 1] = faster_fibonacci(n - 1, m)

    return m[n - 1] + m[n - 2]  # recursive call


print(faster_fibonacci(1000))
print(fibonacci(35))

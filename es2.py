import hello


def is_primo(x):
    flag_primo = True
    for i in range(2, x):
        if x % i == 0:
            flag_primo = False
            break
    if flag_primo:
        return True
    return False


if __name__ == '__main__':

    # nmeri da 1 a mille
    for i in range(1, 11):
        print(i)

    # numeri dispari
    for i in range(1, 1000):
        if i % 2 == 1:
            print(i)

    for i in range(1, 10):
        for j in range(1, 10):
            print(i, "*", j, "=", i * j)

    # vede se x è primo
    x = int(input())

    if is_primo(x):
        print("primo")
    else:
        print("non primo")

    # numeri primi fino a 1000
    for num in range(1, 20):
        if is_primo(num):
            print(num)

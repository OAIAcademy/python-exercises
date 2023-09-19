# if - condition execution
a = 1
b = 2
if a == b:
    print("First case")
elif a > b:  # only checked previous conditions are false
    print("Second case")
else:  # always executed if all others are false
    print("Else")

# Cycle - while
i = 0
while i < 10:
    print(i)
    i += 1  # like writing i = i + 1

# or using a flag
flag = True
i = 0
while flag:
    if i == 10:
        flag = False
    print(i)
    i += 1
# Cycle - for
for i in range(0, 10):  # using generator
    print(i)

for i in [0, 1, 2, 3, 4, 6, 7, 8, 9]:  # using list
    print(i)
# Cycle - nesting
for i in range(0, 10):
    for j in range(0, 10):  # restart every outside cycle
        print(i, j)

# Cycle - unstructured programming
i = 0
while True:
    if i == 5:
        i += i
        continue  # jump to the next cycle
    if i == 10:
        break  # exit from the loop now
    print(i)
    i += i

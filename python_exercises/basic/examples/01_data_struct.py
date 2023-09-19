# list

l = []  # empty declaration
l1 = [1, 2, 3, "asd", 2.3, [2, 3]]  # declaration and non empty init
l1.append(2)  # add to the end
l1.pop(3)  # take out nth

l1[3] = "adbsdfgh"  # change specific value

l1.extend([3, 5])  # append list to list

for i in l1:  # cicle list values
    print(i)

l2 = [(i * 2) for i in range(0, 10)]  # list can be defined inline
print(l2)

#           list can be sliced (select sub string) using [start:end:step]
print(l2[2:4])  # select from 2 to 4
print(l2[:4])  # select till index 4
print(l2[2:])  # select from index 2
print(l2[::2])  # select even index
print(l2[-1])  # select last (very useful!)

# tuple


t = (2, "a", 3)  # definition
a, b = (2, 3)  # unpacking
b, a = a, b  # swap using hidden tuple
_, c = (1, 2)  # throw away first value

# set
s = {"a", 2, 3}
s1 = {"a", 1, 3}
s.add("fsdf")
s.remove("a")
s.intersection(s1)

# dict
d = {"a": 23, "b": {}, 1: []}

d["a"] = 3
d["nuova"] = 2
print(d["nuova"])

d1 = {i: i * 2 for i in [1, 2, 3]}
print(d1)

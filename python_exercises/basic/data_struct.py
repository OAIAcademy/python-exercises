# list

l = []  # empty declaration
l1 = [1, 2, 3, "asd", 2.3, [2, 3]]  # declaration and non empty init
l1.append(2)  # add to the end
l1.pop(3)  # take out first

l1[3] = "adbsdfgh"  # change specific value

l1.extend(l1)  # append list to list

for i in l1:  # cicle list values
    print(i)

l2 = [(i * 2) for i in range(0, 10)]  # list can be defined inline
print(l2)

# tuple

t = (2, "a", 3)

a, b = (2, 3)

# set
s = {"a", 2, 3}
s1 = {"a", 1, 3}
s.add("fsdf")
s.remove("a")

# dict
d = {"a": 23, "b": {}, 1: []}

d["a"] = 3
d["nuova"] = 2
print(d["nuova"])

d1 = {i: i * 2 for i in [1, 2, 3]}
print(d1)

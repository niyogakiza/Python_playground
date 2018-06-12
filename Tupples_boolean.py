# Tuples are immutable sequences.
# Sets are unordered collections of unique elements.
# Booleans are just True and False

#Booleans

True
False

0
1

# Tuples immutable can't be changed as you change list variables
t = (1, 2, 3)
print(t[0])
print(t)


# Sets elements are unordered, repeated elements will be not be repeated in the set.
x = set()

x.add(7)
x.add(5)
x.add(90)
x.add(-2)
x.add(90)
x.add(90)
print(x)

converted = set([1, 3, 4, 5, 6, 7, 8, 88])  # convert set to another array
print(converted)
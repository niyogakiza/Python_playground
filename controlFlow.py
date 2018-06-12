# Control flow: There's no === sign in python
# Equality
1 == 1  # true
1 == '1'  # false

'hi' == 'bye'  # false

# Inequality
1 != 3  # true

# AND
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)

# Don't worry about () in if statements, : shows to start a new code block

if 1 < 2:
    print('yes')
# Nested if statements
if 1 < 2:
    if 2 < 3:
        print("True")

if 1 < 3:
    print('First Block')
    if 20 < 3:
        print('Second Block')  # This line won't execute because is the first was true

if 6 < 4:
    print('First Block')  # from this line to the next code  will be unreachable
    if 30 < 50:
        print('Second Block')

# if else

if 1 < 2:
    print("hello")
else:
    print("last")  # unreachable because the first line is true

if 3 > 6:
    print("I don't believe it.")
else:
    print("Da vero")  # This line will be reachable and printed out

#  else if
if 1 > 3:
    print("Oh non!")
elif 3 == 3:
    print('True')
else:
    print("Nothing found")

# For Loops

seq = [1, 2, 3, 4, 5, 6]
for item in seq:
    print(item)

d = {
    "Sam": 1,
    "Frank": 2,
    "Dan": 3
}
for k in d:  # k stands for key
    print(k)
    print(d[k])

mypairs = [(1, 3), (3, 5), (87, 98)]
for item in mypairs:
    print(item)  # will print them in pairs

for tup1, tup2 in mypairs:  # tuple and parking
    print(tup1)
    print(tup2)

# While loops

i = 1
while i < 5:
    print(" i is: {}".format(i))  # without {} you don't get i
    i = i + 1
    # outputL: i is: 1
    #  i is: 2
    #  i is: 3
    #  i is: 4

# Range function
range(5)  # will get range(0, 5)

a = list(range(0, 5))
print(a)  # [0, 1, 2, 3, 4]

k = list(range(0, 20, 2))
print(k)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] with interval of two

k = list(range(0, 21, 2))
print(k)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] including 20

for item in range(11):
    print(item)  # Prints 0 - 10

# List Comprehension
x = [1, 2, 3, 4]
# out = []
# for num in x:
#     out.append(num**2)
#     print(out)
#     [1]
#     [1, 4]
#     [1, 4, 9]
#     [1, 4, 9, 16]

out = [num**2 for num in x]  # List Comprehension
print(out)  # [1, 4, 9, 16]






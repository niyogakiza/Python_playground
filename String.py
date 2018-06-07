# Strings
# "Strings are a immutable"



# Basics
'hello'
"hello"

"I'm a man"

# Indexing
mystring = 'some guy'
print(mystring[-1])

# Slicing
mystring = 'some guy'
print(mystring[2:]) # me guy
print(mystring[4:]) # guy
print(mystring[:3]) # som
print(mystring[2:5]) # me
print(mystring[::]) # some guy
print(mystring[:]) # some guy
print(mystring[::2]) # sm u


# Basic Methods

x = mystring.upper()
print(x) # SOME GUY

y = mystring.lower()
print(y) # some guy

x = mystring.capitalize()
print(x) # Some guy

myqueen = "Hello Guys!"
k = myqueen.split()
print(k) # ['Hello', 'Guys!']
k = myqueen.split('!')
print(k) # ['Hello Guys', '']

# Print Formatting
w = "Insert another string here: {}".format('INSERT ME!')
print(w) # Insert another string here: INSERT ME!

h = "Item one: {} \n Item two: {}".format("TV", "CAR")
print(h) # Item one: TV
         # Item two: CAR
o = "Item one: {y} \n Item two: {x}".format(x = "TV", y= "CAR")
print(o)
o = "Item one: {x} \n Item two: {y}".format(x = "TV", y= "CAR")
print(o)

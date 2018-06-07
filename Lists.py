# Lists
mylist1 = [1,2,3]
print(len(mylist1)) # len is 3 item in the list

mylist = ['Some more text',1,2,3,4,5,True,'sjdhf',[76,8,90]]
print(mylist)
print(mylist[8]) # [76, 8, 90]
print(mylist[0]) # Some more text
print(mylist[:5]) # ['Some more text', 1, 2, 3, 4]

mylist[0] = "NEW TEXT HERE"
print("after reassignment:")
print(mylist) # ['NEW TEXT HERE', 1, 2, 3, 4, 5, True, 'sjdhf', [76, 8, 90]]
mylist.append("I WILL BE AT THE END OF THE LIST")
print(mylist) # ['NEW TEXT HERE', 1, 2, 3, 4, 5, True, 'sjdhf', [76, 8, 90], 'I WILL BE AT THE END OF THE LIST']
mylist1.append(["hee","ohh", "hahah"])
print(mylist1) # [1, 2, 3, ['hee', 'ohh', 'hahah']]

mylist2 = ["I am in the second list", " yeah i know"]
mylist1.extend(mylist2)
print(mylist1) # [1, 2, 3, ['hee', 'ohh', 'hahah'], 'I am in the second list', ' yeah i know']
item = mylist1.pop()
ha= mylist1.pop(3) # ['hee', 'ohh', 'hahah']
print(ha)
print(item) # yeah i know
print(mylist1) #[1, 2, 3, 'I am in the second list']
mylist1.reverse()
print(mylist1) # ['I am in the second list', 3, 2, 1]
mylist1.copy()
print(mylist1)

numbers = [35,34,57,0,6,349,53,24,35,6,2,38,756,9783]
numbers.sort()
print(numbers) #[0, 2, 6, 6, 24, 34, 35, 35, 38, 53, 57, 349, 756, 9783]

# Nested list
mylistnested = [1,2,['x','h', 'l']]
print(mylistnested[2][1]) # h

# Lists comprehension
matrix = [[1,2,3], [4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col) # [1, 4, 7]


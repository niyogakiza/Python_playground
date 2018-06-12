# Dictionaries
my_stuff = {
    "key1": "value",
    "Key2": "value2",
    "key3": {
        '123':
            [
                234,
                34,
                "LandLover"
            ]
    }
}
print(my_stuff["key1"])
print(my_stuff['key3']['123'][2])  # outPut: LandLover

my_stuff_two = {'Lunch': 'burger', 'Bfast': 'Eggs'}
print(my_stuff_two['Lunch'])
my_stuff_two['dinner'] = 'pasta'
print(my_stuff_two)

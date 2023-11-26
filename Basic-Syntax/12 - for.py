list = ["One" , "Two" , "Three"]
text = "Hello World"

for item in list:
    print(item)

print()

for letter in text:
    print(letter)

print()

# print range
for (index) in range(10):
    print(index)

print()

# print range from 3 -> before 10
for (index) in range (3 , 10):
    print(index)

print()

# print range from 1 -> length of list
for index in range(1 , len(list)):
    print(list[index])


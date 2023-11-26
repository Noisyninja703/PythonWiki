text1 = "HellO WorlD"

text2 = "hello world"

# change casing
print(text1.upper())
print(text1.lower())

# check casing
print(text2.upper().isupper())

# get letter index (string as byte array)
print(text1.index("W"))

# find and replace specific set of characters
print(text1.replace("HellO" , "Hi"))
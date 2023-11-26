
def translate(text):
    output = ""
    # check each letter in str as char array
    for letter in text:
        # if letter matchs vowel -> censor | else -> add letter to final str
        if letter in "AEIOUaeiou":
            if letter.isupper():
                output = output + "*"
            else:
                output = output + "#"
        else:
            output = output + letter
    return output


input = input("Enter a Text : ")
print(translate(input))
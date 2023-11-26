# try to enter an invalid interger value | or changing answer to = 10 / 0
try:
    answer = 10 / 1
    input = input("Enter a number : ")
    input = int(input)

# trying to divide by zero
except ZeroDivisionError as err:
    print(err)

# invalid int
except ValueError:
    print("Error")
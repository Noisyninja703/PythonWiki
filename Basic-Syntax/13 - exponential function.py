
def power(base , pow):
    answer = 1
    # loop until iter of 'pow' are met
    for index in range(pow):
        answer = answer * base
    return answer

print(power(2 , 14))
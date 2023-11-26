
grid = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9],
    [10 , 11]
]

"""
for row in grid:
    print(row)
"""
# iter rows
for row in grid:
    # iter cols
    for col in row:
        # print col value
        print(col)
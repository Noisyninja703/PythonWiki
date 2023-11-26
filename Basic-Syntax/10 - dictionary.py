# init
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# get specific value using key
print(dict["brand"])
print()

# init 2nd dict
con = {
    1 : "One",
    2 : "Two",
    "Three" : 3,
    "no" : 0,
    "jan" : "January",
    "feb" : "February"
 }

# get specific values
print(con.get("jan")) # entry found
print(con.get("ja")) # no valid entry found
print(con.get("ja" , "not found")) # set default value if none returned
print(con.get(1)) # get by int key

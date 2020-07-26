# 7/25/2020 Saidakbar P
# Memory, Algorithms, Binary Search
# Now, we can convert b from a string to a binary number with the int function. We'll need to set the optional second argument, base, to 2 (binary is base two).
print(int(b, 2))
base_10_100 = int("100", 2)
x=int(b, 2)

def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]
# We can use the ord() function to get the integer for an ASCII character.
ord('a')
# The bin function adds "0b" to the beginning of a string to indicate that it contains binary values.
bin(ord('a'))
# We can make a string with some Unicode values
superman = "Clark Kent␦"
# We end up with a sequence of bytes instead of a string
superman_bytes = "Clark Kent␦".encode("utf-8")
# Just like the earlier binary_add function, this adds two hexadecimal numbers
def hexadecimal_add(a, b):
    return hex(int(a, 16) + int(b, 16))[2:]

hulk_bytes = "Bruce Banner␦".encode("utf-8")

# We can't mix strings and bytes
# For instance, if we try to replace the Unicode ␦ character as a string, it won't work, because that value has been encoded to bytes
try:
    hulk_bytes.replace("Banner", "")
except Exception:
    print("TypeError with replacement")
# We can create objects of the bytes data type by putting a b in front of the quotation marks in a string
hulk_bytes = b"Bruce Banner"
# Now, instead of mixing strings and bytes, we can use the replace method with bytes objects instead
hulk_bytes.replace(b"Banner", b"")

thor_bytes = "Thor".encode("utf-8")

# Find the length of a list
def length(ls):
    count = 0
    for elem in ls:
        count = count + 1
length_time_complexity = "linear"

# Check whether a list is empty -- Implementation 1
def is_empty_1(ls):
    if length(ls) == 0:
        return True
    else:
        return False
is_empty_1_complexity = "linear"

# Check whether a list is empty -- Implementation 2
def is_empty_2(ls):
    for element in ls:
        return False
    return True
is_empty_2_complexity = "constant"
# Binary search
# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the data set
length = len(nba)

# Implement the player_age function. For now, just return what the instructions specify
def player_age(name):
    name = format_name(name)
    # Set the initial upper bound of the search
    upper_bound = length - 1
    # Set the initial lower bound of the search
    lower_bound = 0
    # Set the index of the first split (remember to use math.floor)
    index = math.floor((lower_bound+upper_bound)/2)
    # First guess at index (remember to format the guess)
    guess = format_name(nba[index][0])
    # Run search code until the name is equal to the guess, or upper bound is less than lower bound
    while name!=guess and upper_bound>=lower_bound:
        # If name comes before the guess
        if name<guess:
            upper_bound = index - 1
        # Else (name comes after the guess)
        elif name>guess:
            lower_bound = index + 1
        # Set the index of our next guess (remember to use math.floor)
        index = math.floor((lower_bound+upper_bound)/2)
        # Retrieve and format our next guess
        guess = format_name(nba[index][0])
    ### Now that our loop has terminated, we must find out why ###
    # If the name is equal to the guess
    if name==guess:
        return nba[index][2]
        # Return the age of the player at index (column index 2 in data set)
    # Else
    else:
        return -1
        # Return -1, because the function didn't find our player
        
curry_age = player_age("Stephen Curry")
griffin_age = player_age("Blake Griffin")
jordan_age = player_age("Michael Jordan")
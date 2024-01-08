# Technical task steps
# 1. two strings a and b
# 2. merge string in alternative order
# 3. it should start with string a
# 4. if one string a <> b append remaining letter at the end 


# pseudo code

# create new variable which will hold new string
# check the length of both strings 
# loop over index of smaller string
    # print value of first index of a
    # print value of same index of b

# add remaining chars into the string from a or b

# if a is smaller

# create new variable 
# add first char of a
# add first char of b
# add second char of a
# add second char of b
# add remaining chars of b
a = 'ab'
b = 'pqrs'
max_len = len(a) if len(a) > len(b) else len(b)
new_string = ''
for item in range(0,max_len):
    if len(a) > item:
        new_string += a[item]
    if len(b) > item:
        new_string += b[item]

print(new_string)






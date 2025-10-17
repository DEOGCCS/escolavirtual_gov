width = 10
height = 5

# change int to float
width_float = float(width)
print(type(width))
print(type(width_float))

# change float to string
width_str = str(width_float)
print(type(width_str))

# change string to int
#return_int = int(width_str) Doesn't work because it is 10.0 o 10.
return_int = int(width_float)
print(type(return_int))

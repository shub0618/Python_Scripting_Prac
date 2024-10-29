# Bitwise operators in Python are used to perform bit-level operations on integers. 
# They operate directly on the binary representations of numbers and can be very efficient for certain types of computations. 
# Here's a rundown of Python's bitwise operators:


# Bitwise AND (&)
a = 5  # 0b0101
b = 3  # 0b0011
result = a & b  # 0b0001
print(result)  

# Bitwise OR (|)
a = 5  # 0b0101
b = 3  # 0b0011
result = a | b  # 0b0111
print(result)   

# Bitwise XOR (^)
a = 5  # 0b0101
b = 3  # 0b0011
result = a ^ b  # 0b0110
print(result)  

# Bitwise NOT (~)
a = 5  # 0b0101
result = ~a  # 0b1010 (in two's complement: -6)
print(result)  

# Bitwise Left Shift (<<)
a = 5  # 0b0101
result = a << 1  # 0b1010
print(result)   

# Bitwise Right Shift (>>)
a = 5  # 0b0101
result = a >> 1  # 0b0010
print(result)   







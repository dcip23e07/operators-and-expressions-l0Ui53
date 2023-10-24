# 1
a = 4999
print(bin(a)) 
a2 = 0b1001110000111

# 2
b = 2111
print(bin(b)) 
b2 = 0b100000111111

# 3 what will be the value of 4999 & 2111
# 0b1001110000111 &
#  0b100000111111
#  0b000000000111 result in base-2
#  result in b-10
print(a & b)

# 4 what will be the value of 4999 | 2111
# 0b1001110000111 OR
#  0b100000111111
#  0b101111111111 result in base-2
print(a or b)
print(bin(a or b))


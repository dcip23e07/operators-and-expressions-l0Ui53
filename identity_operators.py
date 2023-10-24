var_a = 400 
var_b = '200' + '200' 
var_c = 400.0 
var_d = 200 + 200

# 1
# i. 
var_a == var_b # False because str and int cannot be compared mathematically
# ii. 
var_a is var_b # False because point to different objects

# 2
# i. 
var_a == var_c # True because mathematically equal
# ii. 
var_a is var_c # False because point to different objects

# 3
# i.
print(var_a == var_d) # True because mathematically equal
# ii. 
print(var_a is var_d) # True because points to the same object
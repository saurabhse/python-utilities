"""
find substring
"""
str_var = """
a
b
[c]
d
e
"""
value = str_var[str_var.find("[")+1:str_var.rfind("]")]
print(value) #this will print c

"""
partition string
"""

str_var = "a b"
head, sep, tail = str_var.strip().partition(" ")
print(head) # a
print(sep)  # space
print(tail) # b

str_var = "a b c"
head, sep, tail = str_var.strip().partition(" ")
print(head) # a
print(sep)  # space
print(tail) # b c

""" convert list to set """

list_var = [1,2,3]
set_var = set(list_var)

""" convert list to string """

list_var = [1,2,3]
str_var = ",".join(list_var)

""" add string variable to all elements of list """
list_var = ['a','b','c']
new_list_var = map(lambda list_elem: list_elem + " dynamic_string", list_var)
print(','.join(new_list_var)) # a dynamic_string,b dynamic_string,c dynamic_string


""" cast data to type and convert to list"""
ids = list(map(int,ids))

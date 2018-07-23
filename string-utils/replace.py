# replace in string using lists
def replace(combined_list,str_1,str_2,record_count):
  count = 1
  for row in itertools.zip_longest(*combined_list):
    first = str_1
    second  = str_2
    for i in range(0,len(row)):
      rowval = row[i]
      if record_count != count:
        first = first.replace("#wildcard"+str(i),rowval)
        text = first
      else:
        second = second.replace("#wildcard"+str(i),rowval)
        text = second
  count = count+1
  yield text
  
if __name__ == "main":
  list_1 = [1,2,3]
  list_2 = ['a','b','c']
  combined_list = [list_1,list_2]
  str_1 = "select #wildcard1, #wildcard2 from dual union all"
  str_2 = "select #wildcard1, #wildcard2 from dual"
  replace(combined_list,str_1,str_2,len(list_1))

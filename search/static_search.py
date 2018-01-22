"""
  Use dict to search for static strings
  if search_str is not found return None
"""
def fetch_value(search_str):
  return {
    'abc' : '123'.
    'xyz' : '456'
  }.get(search_str,None)
  
if __name__ == '__main__':
  val = fetch_value('abc')
  val = fetch_value('xyz')

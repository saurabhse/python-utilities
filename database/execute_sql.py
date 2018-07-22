
def execute(con,cursor,sql_queries):
  sql_queries_list = sql_queries.split(;)
  for sql in sql_queries_list:
    if len(sql.strip()) == 0:
      print("please pass sql")
    else:
      try:
        cursor.execute(sql)
        con.commit()
      except cx_Oracle.DatabaseError as exception:
        exit(1)
        
        
if __name__ == "main":
  con,cursor = connect_db() # call connect module
  execute(con,cursor,'delete table orders')
  cleanup(con,cursor) # call connect module

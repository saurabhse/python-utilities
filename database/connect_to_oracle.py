"""
Connect to oracle using cx_oracle
"""

import cx_Oracle
def connect_to_db():
	try:
		con = cx_Oracle.connect(db+"/"+dbpwd+"@"+dburl)
		cursor = con.cursor()
	except cx_Oracle.DatabaseError as exception:
		print(exception)
		exit (1)

def cleanup_resources():
	cursor.close()
	con.close()

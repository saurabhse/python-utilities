import cx_Oracle
from profiling import do_cprofile

@do_cprofile(__file__)
def connect_to_db():
	try:
		con = cx_Oracle.connect(db+"/"+dbpwd+"@"+dburl)
		cursor = con.cursor()
	except cx_Oracle.DatabaseError as exception:
		print(exception)
		exit (1)

@do_cprofile(__file__)
def cleanup_resources():
	cursor.close()
	con.close()

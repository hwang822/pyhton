import sqlite3

conn = sqlite3.connect('tuorial.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
	
def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES(14512345, '2018-03-21', 'python', 5)")
	conn.commit()
	c.close()
	conn.close()
	
create_table()
data_entry()	
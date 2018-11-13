import os
import MySQLdb
from flask import Flask, request, json
from flask import session, g
from flask import redirect, url_for, abort
from flask import render_template, flash
from datetime import datetime
import program
from db_config import * 
from db_query_config import * 
from select_class import * 
from query_example import *
#from tables import *
#from interaction import *
import _mysql
from datetime import datetime



DATABASE = "адрес бд в папках"
DEBUG = True #тажа хуйня что и в django
SECRET_KEY = "development key" #ключ безопстности для сайта нельзя ни куда кидать 
USERNAME = "admin"
PASSWORD = "default"

app = Flask(__name__)
app.config.from_object(__name__)
conn = MySQLdb.connect("localhost", "root", "1", "flask_db")
cursor = conn.cursor()

"""app.config.update(dict(
	DATABASE = os.path.join(app.root_path, "путь и имя бд"),
	DEBUG = True,
	SECRET_KEY = "development key",
	USERNAME = "admin",
	PASSWORD = "default",
	))"""

'''def connect():
	try:
		conn = MySQLdb.connect("localhost", "root", "1", "flask_db")
		cursor = conn.cursor()
		return cursor
	except:
		print ("Connection ERROR")
	pass
#Произведение запроса - возвращает результат (объект _mysql.connection.use_result)
def query(query_string):
	try:	
		cursor = connect()
		result = cursor.execute(query_string)
		print (query_string)
		if result:
			return result
		else:
			print (query_string)
			print ("\n Wrong query")
			pass
	except:
		print('hueta')
		pass
	return result
'''
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def main():
	return render_template("order.html")
@app.route('/stat')
def stat():
	return render_template("stat.html")	

@app.route("/", methods=["POST"])
def order_add():
	_time = request.form['time_of_start_order']
	_price = float(request.form['price'])
	_table = int(request.form['table'])
	_comit = request.form['comit']
	if _time and _price and _table and _comit:
		insert_into("stol", ["time_of_start_order", "price", "table_of_order", "comit"], [_time, _price, _table, _comit])
		#query("insert into stol(time_of_start_order, price, table_of_order, comit) values('%s', '%f', '%d', '%s')" % (_time, _price, _table, _comit))
		return render_template("order.html")
	elif _price and _table and _comit:
		_time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
		insert_into("stol", ["time_of_start_order", "price", "table_of_order", "comit"], [_time, _price, _table, _comit])
		#query("insert into stol(time_of_start_order, price, table_of_order, comit) values('%s', '%f', '%d', '%s')" % (_time, _price, _table, _comit))
		return render_template("order.html")
	else:
		return json.dumps({"html":"<p>jeppa</p>"})

@app.route('/statistic')
def pok():
	return render_template('statistic.html')
#функция которая будет осушествлять сортировку по бд
#возрашает колво позиций 
#ну и собстсвенно сами позиции шаришь 
'''number_of_order = 10
_price = 800
_table = 12
_comit = "солидно епт"'''
_timeStart = 0
_timeEnd = 0
@app.route("/stat", methods=["POST"])
def pokaz():
	_timeStart ="'" + str(request.form['1time_of_start']) 
	_timeEnd = "'" + str(request.form['1time_of_end'])
	_timeStart = _timeStart.replace ("T", " ")
	_timeEnd = _timeEnd.replace ("T", " ")
	_timeStart += ":00'"
	_timeEnd += ":00'"
	if _timeStart:
		if _timeEnd:
			i_t = "stol"
			i_cl = ["id", "time_of_start_order"]
			list_ct = ["time_of_start_order", "time_of_start_order"]
			list_o = [">", "<"]
			list_v = [_timeStart, _timeEnd]
			list_le = ["", "AND"]
			q = set_select_where_combined (i_t, i_cl, list_ct, list_o, list_v, list_le)
			d = do_select(q)
			number_order = d.k
			#number_order = query("select table_of_order, price, time_of_start_order, comit from stol where time_of_start_order > '%s' and time_of_start_order < '%s'" % (_timeStart, _timeEnd)))
			try:
				number_of_order = len(number_order)
			except TypeError:
				if number_order == None:
					number_of_order = 0
				else:
					number_of_order = 1
		else:
			_timeEnd = datetime.now()
			try:
				number_of_order = len(number_order)
			except TypeError:
				if number_order == None:
					number_of_order = 0
				else:
					number_of_order = 1
			
			tuple1.append(d.k)
			return render_template('statistic.html')
	else:
		return json.dumps({"html":"<p>jeppa</p>"})
'''if _timeStart:
		if _timeEnd:
			print("hui")
			i_t = "stol"
			i_cl = ["id", "time_of_start_order"]
			list_ct = ["time_of_start_order", "time_of_start_order"]
			list_o = [">", "<"]
			list_v = [_timeStart, _timeEnd]
			list_le = ["", "AND"]
			q = set_select_where_combined (i_t, i_cl, list_ct, list_o, list_v, list_le)
			d = do_select(q)
			number_order = d.k
			#number_order = query("select table_of_order, price, time_of_start_order, comit from stol where time_of_start_order > '%s' and time_of_start_order < '%s'" % (_timeStart, _timeEnd)))
			try:
				number_of_order = len(number_order)
			except TypeError:
				if number_order == None:
					number_of_order = 0
				else:
					number_of_order = 1
		else:
			_timeEnd = datetime.now()
			try:
				number_of_order = len(number_order)
			except TypeError:
				if number_order == None:
					number_of_order = 0
				else:
					number_of_order = 1
			
			tuple1.append(d.k)
else:
	print('error420')'''

#@app.route("/statistic", methods = ["GET"])
#def pokaz1():
	
'''@app.route('/statistic')
def pok():
	return render_template('statistic.html')'''

#@app.route("/")
#@app.route("/stat")
#def stat():
#	return render_template("stat.html")	



if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=1111)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _mysql
encoding = "utf-8" 

#Подключение к БД, возвращает объект _mysql.connection

def connect():
	
	conn = _mysql.connect(host='localhost', 
							db='flask_db', 
							user='root',
							passwd='1'
							)
	conn.set_character_set('utf8')
	#print(_mysql.connection.get_character_set_info(conn))
	#print (conn)
	return conn
	
#Произведение запроса - возвращает результат (объект _mysql.connection.use_result)
def query(query_string):
	
	db = connect()
	db.query(query_string)
	
	return db.use_result()

def query_insert(query_string):
	
	db = connect()
	db.query(query_string)
	last_id = db.insert_id()
	return last_id

def query_db(query_string):
	
	db = connect()
	db.query(query_string)
	
	return db

#a = query_insert("INSERT INTO Course (unit_name, comment) VALUES('123', '456');")
#print (a)
#левые строки
# db = connect()


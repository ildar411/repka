#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from db_config import * 
import _mysql
encoding = "utf-8" 

# INSERT INTO Query - запрос инсерт от таблицы, списка колонок, списка ввода

def insert_into (tablename, column_list, insert_list):
	
	query_string = "INSERT INTO " + tablename  + " ("
	
	for x in column_list:
		#print (x)
		query_string = query_string + str(x) + ", "
		
	query_string = query_string[0: len(query_string) - 2] + ") VALUES (" ;
	
	for x in insert_list:
		#print (x)
		query_string = query_string + "'{a}', "
		query_string = query_string.format(a = x)
		
	query_string = query_string[0: len(query_string) - 2] + ");";

	print(query_string)
	
	return query_insert(query_string)

def update_by_id (tablename, column_list, insert_list, where_id):
	
	query_string = "UPDATE " + tablename  + " SET "
	
	for i in range(len(column_list)):
		#print (x)
		query_string = query_string + str(column_list[i]) + "="
		query_string = query_string + "'{a}', "
		query_string = query_string.format(a = str(insert_list[i]))
		query_string = query_string[0: len(query_string) - 2]
		query_string = query_string + " WHERE id = " + str(where_id);
	print(query_string)
	query(query_string)

	return  where_id
	
	
# SELECT Simple Query - просто вывод колонок
	
def select_simple_query (tablename, column_list):
	
	query_string = "SELECT " 
	
	for x in column_list:
		print (x)
		query_string = query_string + x + ", "		
		
	query_string = query_string[0: len(query_string) - 2] + " FROM " + tablename + ";";

	print(query_string)
	
	return query(query_string)
	
# Эта функция выводит селект в терминальную таблицу
def select_simple_show (query, tablename, column_list):

	r = query.fetch_row(0) #эта штука выдает список кортежей (строк результата запроса)
	s = "\n"*3 + tablename + "\n"*2 
	for x in column_list:
		s = s + x + " "*(20 - len(x.decode('utf-8'))) + "|"
	s = s + "\n"
	for x in column_list:
		s = s + "_" * 20 + "|" 
	s = s + "\n"
	for x in r:
		for y in range (len(column_list)):
			if x[y] == None:
				w = "NULL"
			else:
				w = x[y]
			s = s + w + " "*(20 - len(w.decode('utf-8'))) + "|"
		s = s + "\n"
	s = s + "\n" 
	
	return s

#Чисто выводит в строку все элементы из селекта
def select_simple_check (query, tablename, column_list):

	r = query.fetch_row(0)
	
	for x in r:
		for y in range (len(column_list)):
			if x[y] == None:
				w = "NULL"
			else:
				w = x[y]
			print(w + " ")
	pass

def get_column_list (tablename):
	query_string = "SHOW COLUMNS FROM " + tablename
	out = query(query_string).fetch_row(0)
	present = []
	for x in out:
		present.append(x[0])
	return present

#левые строки
#print (get_column_list ("Exercise"))
	
#f = open("123.txt", "a+")
#t = "Course"
#cl = ["id", "comment"]
#q = select_simple_query (t, cl)
#qs = select_simple_show (q, t, cl)
#print(_mysql.connection.get_character_set_info(q))
#print (qs)
#f.close ()


    



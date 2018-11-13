#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from db_config import * 
from db_query_config import * 
from select_class import * 
import _mysql
encoding = "utf-8" 

def set_select_where_simple (i_t, i_cl, i_ct, i_o, i_v):
	
	q = Select()
	q.set_tablename(i_t)
	q.set_column_list(i_cl)
	q.set_created_where_expression(i_ct,i_o,i_v)
	
	return q
	
def set_change_where_expression (q, list_ct, list_o, list_v, list_le):
	q.clear_where_expressions_list()
	for i in range (len(list_ct)):
		e = q.create_where_expression(list_ct[i],list_o[i],list_v[i])
		q.append_where_expressions_list(e, list_le[i])
		q.combine_where_expressions()
	#print q.k
	return q
	
	
def set_select_where_combined (i_t, i_cl, list_ct, list_o, list_v, list_le):
	print ("zdarova")
	q = Select()
	q.set_tablename(i_t)
	q.set_column_list(i_cl)
	set_change_where_expression(q, list_ct, list_o, list_v, list_le)
	#print q.k
	return q


def set_select_default (i_t,i_cl):
	
	q = Select()
	q.set_tablename(i_t)
	q.set_column_list(i_cl)
	
	return q

def do_select (q):
	
	q.select_simple_query ()
	#q.select_simple_show ()
	
	return q


	
def user_input(text):
	print("Input " + str(text))
	var = raw_input()
	
	return var

def conditional_input (input_list):
	a = input()
	for x in input_list:
		if a == x:
			return a
	print ("Repeat input")
	conditional_input (input_list)
	pass 



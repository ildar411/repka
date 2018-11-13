#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
from db_config import * 
from db_query_config import * 
import _mysql
encoding = "utf-8" 

class Select:
	def __init__(self):
	
		self.query_string = ""
		self.tablename = "Cource"
		self.variatives = []
		self.where_expression = "1 = 1"
		self.query_result = 0
		self.where_expressions_list = []
		self.column_list = []
		self.k = []

	
	def set_tablename (self, tablename):
		self.tablename = tablename
		
		return self.tablename
	
	def set_column_list (self, column_list):
		if column_list == ["*"]:
			self.column_list = get_column_list (self.tablename)
		else:
			self.column_list = column_list
		
		return self.column_list
	
	def add_variative (self, variative):
		self.variatives.append(variative)
		
		return variative
		
	def pop_variative (self):
		
		return self.variatives.pop()
		
	def clear_variative_list (self):
		self.variatives.clear()
		
		return self.variatives
		
	def create_where_expression (self, column, where_operator, variative):
		where_expression = str(column) + str(where_operator) + str(variative)
		
		return where_expression
	
	def set_where_expression (self, where_expression):
		self.where_expression = where_expression
			
	def set_created_where_expression (self, column, where_operator, variative):
		self.where_expression = self.create_where_expression (column, where_operator, variative)
		
		return self.where_expression
	
	def append_where_expressions_list (self, where_expression, logical_element):
		self.where_expressions_list.append(logical_element)
		self.where_expressions_list.append(where_expression)
		
		pass
		
	def combine_where_expressions (self):
		self.where_expression = ""
		for x in self.where_expressions_list:
			self.where_expression += x + " "
			if self.where_expression == " ":
				self.where_expression = ""
		
		return self.where_expression
	
	def clear_where_expressions_list (self):
		self.where_expressions_list = []
		
		pass
		
	def select_simple_query (self):
		self.query_string = "SELECT "
		for x in self.column_list:
			print("asd")
			print(x)
			self.query_string = self.query_string + x + ", "		
		
		self.query_string = self.query_string[0: len(self.query_string) - 2] + " FROM " + self.tablename + " WHERE " + self.where_expression + ";" 
		print(self.query_string)
		
		self.query_result = query(self.query_string)
		self.k = self.query_result.fetch_row(0)
		
		return self.k
		
	def select_simple_show (self):
		#r = self.query_result.fetch_row(0)
		#self.k = r
		r = self.k
		s = "\n"*3 + self.tablename + "\n"*2 
		for x in self.column_list:
			s = s + x + " "*(20 - len(x.decode('utf-8'))) + "|"
		s = s + "\n"
		for x in self.column_list:
			s = s + "_" * 20 + "|" 
		s = s + "\n"
		for x in r:
			for y in range (len(self.column_list)):
				if x[y] == None:
					w = "NULL"
				else:
					w = x[y]
				s = s + w + " "*(20 - len(w.decode('utf-8'))) + "|"
			s = s + "\n"
		s = s + "\n" 
		#print s
	
	def return_results (self):
		return self.k




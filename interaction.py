#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from db_config import * 
from db_query_config import * 
from select_class import * 
from query_example import *
from tables import *
import _mysql

class Interaction():
	
	def __init__ (self):
		self.asd = ""
	
	def create_table (self, name):
		
		NewTable = Table_Present()
		NewTable.TableName = name
		NewTable.create_table()
		
		pass
	
	def rename_table (self, name, where_id):
		
		NewTable = Table_Present()
		NewTable.TableName = name
		NewTable.rename_table(where_id)
		
		pass
	
	def enable_table (self, where_id):
		
		NewTable = Table_Present()
		NewTable.change_status(where_id, "active")
		
		pass
	
	def disable_table (self, where_id):
		
		NewTable = Table_Present()
		NewTable.change_status(where_id, "disable")
		
		pass
	
	def add_employee (self, name, comment):
		
		NewEmployee = Employee()
		NewEmployee.EmployeeName = name
		NewEmployee.EmployeeComment = comment
		NewEmployee.create_employee()
		
		pass
	
	def add_salary_rule (self,  salary_derivative, salary_argument, Employee_id):
		NewSalaryRule = Employee_Salary_Rule() 
		NewSalaryRule.RuleSalary_derivative = salary_derivative
		NewSalaryRule.RuleSalary_argument = salary_argument
		NewSalaryRule.RuleEmployee_id = Employee_id
		NewSalaryRule.create_unit()
		NewSalaryRule.update_salary_derivative(salary_derivative, NewSalaryRule.ClassId)
		NewSalaryRule.update_salary_argument(salary_argument, NewSalaryRule.ClassId)
	
		pass
	
	def rename_salary_rule (self, name, where_id):
		NewSalaryRule = Employee_Salary_Rule() 
		NewSalaryRule.update_rule_name(name, where_id)
		
		pass
	
	def start_work (self, Employee_id, datetime_start):
		WorkTime = Employee_Worktime()
		WorkTime.WorkTime_Employee_id = Employee_id
		WorkTime.WorkTime_start = datetime_start
		WorkTime.create_unit()
		a = WorkTime.return_id()
		WorkTime.update_start_time(WorkTime.ClassId)
		
		pass
	
	def end_work (self, datetime_end, salary_rule_id):
		WorkTime = Employee_Worktime()
		WorkTime.ClassId = WorkTime.get_last_worktime_id()
		WorkTime.WorkTime_Employee_Salary_Rule_id = salary_rule_id
		WorkTime.WorkTime_end = datetime_end
		WorkTime.update_end_time(WorkTime.ClassId)
		WorkTime.update_rule_by_id(WorkTime.ClassId)
		
		pass
	
	def create_order (self, Employee_id, datetime_created):
		NewOrder = Order()
		NewOrder.OrderEmployee_id = Employee_id
		NewOrder.self.OrderTime_created = datetime_created
		NewOrder.update_creating_time()
		NewOrder.create_unit()

		return NewOrder.ClassId
	
	def change_order_price (self, price, where_id):
		NewOrder = Order()
		NewOrder.OrderPrice = price
		NewOrder.update_price(where_id)
		
		pass
		
	def change_order_table (self, Table_id, where_id):
		NewOrder = Order()
		NewOrder.OrderTable_id = Table_id
		NewOrder.update_table_id(where_id)
		
		pass
		
	def change_order_employee (self, Employee_id, where_id):
		NewOrder = Order()
		NewOrder.OrderEmployee_id = Employee_id
		NewOrder.update_employee_id(where_id)
		
		pass
		
	def change_order_client_name (self, client_name, where_id):
		NewOrder = Order()
		NewOrder.OrderClient_name = client_name
		NewOrder.update_client_name(where_id)
		
		pass
	
	def close_order (self, order_id, datetime_closed):
		NewOrder = Order()
		NewOrder.OrderClient_name = client_name
		NewOrder.update_closing_time(order_id)
		
		pass
		
NewOrder.OrderTime_closed


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from db_config import * 
from db_query_config import * 
from select_class import * 
from query_example import *
#from tables import *
#from interaction import *
import _mysql
from datetime import datetime

#inter = Interaction()

#inter.create_table (name) - создает стол в бд c именем в name (по умолчанию активный)

#inter.rename_table (name) - меняет имя стола в бд на имя в name

#inter.enable_table ("id") - делает стол активным по id

#inter.disable_table ("id") - выключает стол по id

#inter.add_employee ("Вася", "Солидный") - добавляет Васю Солидного в сотрудники в бд

#inter.add_salary_rule ("day",1500, "id") - добавляет правило выдачи зп в бд для сотрудника с id (1500 в день)

#inter.rename_salary_rule("Васян за два косых", "id") - переименовывает правило выдачи зп

#datetime_start = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") - получает время (начала работы) на сервере в формате "%Y.%m.%d %H:%M:%S"

#inter.start_work ("id", datetime_start) - начало работы сотрудника (его id) фиксируется в бд

#datetime_end = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") - получает время (конца работы) на сервере в формате "%Y.%m.%d %H:%M:%S"

#inter.end_work (datetime_end, "salary_id") - конец работы сотрудника фиксируется в бд c "salary_id" - id правила расчета

#create_order (self, Employee_id, datetime_created):
	#return Order.id
	
#change_order_price (self, price, where_id):

#change_order_table (self, Table_id, where_id):

#change_order_employee (self, Employee_id, where_id):

#change_order_client_name (self, client_name, where_id):

#close_order (self, order_id, datetime_closed):

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from typing import (
	List,
	Tuple
)

# external dependencies
import sqlite3


__author__ = "Henrique Kops && Victoria Tortelli"


class Storage:

	__CREATE_SQL =  '''CREATE TABLE IF NOT EXISTS diffie (a TEXT, key TEXT)'''
	__SET_SQL = '''INSERT INTO diffie (a, key) VALUES (?, ?)'''
	__GET_SQL = '''SELECT a, key FROM diffie LIMIT 1'''

	def __init__(self) -> None:
		self.con = sqlite3.connect("diffie.db")
		self.__execute(self.__CREATE_SQL)

	def __execute(self, cmd:str, args=None) -> List[str]:
		try:
			cur = self.con.cursor()
			if args: cur.execute(cmd, args)
			else: cur.execute(cmd)
			self.con.commit()
			return cur.fetchall()
		except Exception as e:
			print(f"Error at sqlite3: {e}")
		finally:
			cur.close()

	def get(self) -> Tuple[str, str]:
		lst = self.__execute(self.__GET_SQL)
		a = key = None
		if lst:
			a = lst[0][0]
			key = lst[0][1]
		return a, key

	def set(self, a, key) -> None:
		self.__execute(self.__SET_SQL, (str(a), str(key),))

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# external dependencies
import sqlite3


__author__ = "Henrique Kops && Victoria Tortelli"


class Storage:

	__CREATE_SQL =  '''CREATE TABLE IF NOT EXISTS diffie (a text, key text)'''
	__SET_SQL = '''INSERT INTO diffie (a, key) VALUES (?, ?)'''
	__GET_SQL = '''SELECT a, key FROM diffie LIMIT 1'''

	def __init__(self) -> None:
		self.con = sqlite3.connect("diffie.db")
		self.__execute(self.__CREATE_SQL)

	def __execute(self, cmd:str):
		try:
			cur = self.con.cursor()
			cur.execute(cmd)
			self.con.commit()
		except Exception as e:
			print(f"Error at sqlite3: {e}")
		finally:
			cur.close()

	def get(self):
		return self.__execute(self.__GET_SQL)

	def set(self, a, key):
		return self.__execute(self.__SET_SQL, (a, key,))

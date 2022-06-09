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

	__CREATE_SQL =  '''CREATE TABLE IF NOT EXISTS diffie (a TEXT, key TEXT DEFAULT '', creation DATETIME DEFAULT CURRENT_TIMESTAMP)'''
	__SET_SQL = '''INSERT INTO diffie (a) VALUES (?)'''
	__GET_SQL = '''SELECT * FROM diffie ORDER BY creation DESC LIMIT 1'''
	__UPD_SQL = '''UPDATE diffie SET key = ? WHERE a = ?'''

	def __init__(self) -> None:
		self.con = sqlite3.connect("diffie.db")
		self.__execute(self.__CREATE_SQL)

	def __execute(self, cmd:str, args:tuple=None) -> List[str]:
		try:
			cur = self.con.cursor()
			cur.execute(cmd, args) if args else cur.execute(cmd)
			self.con.commit()
			return cur.fetchall()
		except Exception as e:
			print(f"Error at sqlite3: {e}")
		finally:
			cur.close()

	def get_a(self) -> int:
		res = self.__execute(self.__GET_SQL)
		return int(res[0][0]) if res else None

	def get_key(self) -> bytes:
		res = self.__execute(self.__GET_SQL)
		return bytes.fromhex(res[0][1]) if res else None

	def set_a(self, a) -> None:
		self.__execute(self.__SET_SQL, (str(a),))

	def set_key(self, a, key) -> None:
		self.__execute(self.__UPD_SQL, (str(key), str(a),))

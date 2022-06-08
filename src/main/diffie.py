#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from random import randint


__author__ = "Henrique Kops && Victoria Tortelli"


class DiffieHellman:

	def __init__(self, a=None) -> None:
		self.a = randint(10**29, 10**30) if not a else a

	def run(self, g:int, p:int) -> int:
		return pow(g, self.a, p)

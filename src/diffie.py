#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from math import pow

__author__ = "Henrique Kops"


class DiffieHellman:

	def __init__(self, a:int) -> None:
		self.a = a

	def encrypt(self, p:int, g:int) -> None:
		return (pow(g, self.a)) % p

	def decrypt(self, b:int, p:int) -> None:
		return (pow(b, self.a)) % p


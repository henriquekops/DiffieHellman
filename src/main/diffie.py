#!/usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = "Henrique Kops && Victoria Tortelli"


class DiffieHellman:

	def __init__(self, a:int) -> None:
		self.a = a

	def run(self, g, p) -> None:
		return pow(g, self.a, p)
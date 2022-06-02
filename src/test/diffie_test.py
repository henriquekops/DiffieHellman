#!/usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = "Henrique Kops"

import unittest

# project dependencies
from src.main.diffie import DiffieHellman
from src.test.utils import (
	a,
	p, 
	g, 	
	A
)


class TestDiffieHellman(unittest.TestCase):

	def test_encrypt(self):
		d = DiffieHellman(a)
		assert d.run(p, g), A

	def test_decrypt(self):
		pass


if __name__ == "__main__":
	unittest.main()

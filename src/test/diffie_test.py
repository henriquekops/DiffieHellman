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
	A,
	B,
	V
)


class TestDiffieHellman(unittest.TestCase):

	def test_encrypt(self):
		d = DiffieHellman(a)
		assert d.run(g, p), A

	def test_decrypt(self):
		d = DiffieHellman(a)
		assert d.run(B, p), V


if __name__ == "__main__":
	unittest.main()

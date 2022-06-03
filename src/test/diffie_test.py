#!/usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = "Henrique Kops && Victoria Tortelli"

# built-in dependencies
import unittest

# project dependencies
from src.main.diffie import DiffieHellman


class TestDiffieHellman(unittest.TestCase):

	def setUp(self):
		self.a = 123456789012345678901234567890123456789
		self.p = 1041607122029938459843911326429539139964006065005940226363139
		self.g = 10
		self.A = 372039332014874382386471904578699975832029010553081171186923
		self.B = 785637473337331550103697723492144500354289194897294297600528
		self.V = 531549124896866458964697691745629549010303164318920061744393

	def test_encrypt(self):
		d = DiffieHellman(self.a)
		assert d.run(self.g, self.p), self.A

	def test_decrypt(self):
		d = DiffieHellman(self.a)
		assert d.run(self.B, self.p), self.V


if __name__ == "__main__":
	unittest.main()

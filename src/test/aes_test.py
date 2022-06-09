#!/usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = "Henrique Kops && Victoria Tortelli"

# built-in dependencies
import unittest

# project dependencies
from src.main.crypto import AES


class TestAES(unittest.TestCase):

	def setUp(self):
		self.IV = b'RP\xabm\xd2\x8e\xe9\xac\x88\x89\xa4\xd3\xc8\xa6\xd0\xeb'
		self.KEY = b'\x14\x0bA\xb2*)\xbe\xb4\x06\x1b\xdaf\xb6t~\x14'
		self.MSG = b"Basic CBC mode encryption needs padding."
		self.CT = "b53e6fd9cebeebc9152f2aa60361b41dbda1870edafc5023bb6d3187e2\
			fcbfc76da84651283fea311f0465e024a846fb178b86012e754a427b0ec51e1b5a\
			c8c918d4e8b7ff29e485ad3856c9afa7308426e6225577da144ef1cabfd6d48af941"

	def test_encrypt(self):
		aes = AES(self.KEY, self.IV)
		assert aes.encrypt(self.MSG).hex(), self.CT

	def test_decrypt(self):
		aes = AES(self.KEY, self.IV)
		assert aes.decrypt(bytes.fromhex(self.CT)), self.MSG


if __name__ == "__main__":
	unittest.main()

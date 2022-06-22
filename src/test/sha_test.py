#!/usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = "Henrique Kops && Victoria Tortelli"

# built-in dependencies
import unittest

# project dependencies
from src.main.crypto import SHA256


class TestSHA256(unittest.TestCase):

	def setUp(self):
		self.input_V = 531549124896866458964697691745629549010303164318920061744393
		self.expected_V = "f4f4c2f46d031dc7aed44aad9f2b5e94"

	def test_SHA256(self):
		assert SHA256.hash(self.input_V), self.expected_V


if __name__ == "__main__":
	unittest.main()

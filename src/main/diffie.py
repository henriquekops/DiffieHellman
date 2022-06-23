#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from random import randint


__author__ = "Henrique Kops && Victoria Tortelli"


class DiffieHellman:

	def __init__(self, a:int=None) -> None:
		"""algoritmo de troca de chaves Diffie Hellman

		Args:
			a (int, optional): chave privada, padrao nulo
		"""
		self.a = randint(10**29, 10**30) if not a else a

	def run(self, g:int, p:int) -> int:
		"""gerando a chave publica e a chave de criptografia, de acordo com o gerador

		Args:
			g (int): gerador
			p (int): numero primo 

		Returns:
			int: chave publica ou chave de criptografia
		"""
		return pow(g, self.a, p)

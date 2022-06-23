#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from hashlib import sha256

# external dependencies
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.ciphers import (
	Cipher,
	algorithms,
	modes
)

__author__ = "Henrique Kops && Victoria Tortelli"


class AES:

	def __init__(self, key:bytes, iv:bytes) -> None: 
		"""algoritmo de cifragem simetrica AES (cryptography)

		Args:
			key (bytes): chave de criptografia
			iv (bytes): vetor de inicializacao
		"""
		self.iv = iv
		self.padding = PKCS7(block_size=128)
		self.cipher = Cipher(
			algorithm=algorithms.AES(key),
			mode=modes.CBC(iv),
			backend=default_backend()
		)
	
	def encrypt(self, msg:bytes) -> bytes:
		"""criptografa a mensagem usando AES

		Args:
			msg (bytes): mensagem a ser criptografada

		Returns:
			bytes: mensagem criptografada
		"""
		encryptor = self.cipher.encryptor()
		padder = self.padding.padder()
		p_msg = padder.update(msg) + padder.finalize()
		e_msg = encryptor.update(p_msg) + encryptor.finalize()
		return (self.iv + e_msg)

	def decrypt(self, msg:bytes) -> bytes:
		"""descriptografa a mensagem

		Args:
			msg (bytes): mensagem criptografada

		Returns:
			bytes: mensagem descriptografada
		"""
		decryptor = self.cipher.decryptor()
		unpadder = self.padding.unpadder()
		p_msg = decryptor.update(msg) + decryptor.finalize()
		return unpadder.update(p_msg) + unpadder.finalize()


class SHA256:

	@classmethod
	def hash(self, v:int) -> str:
		""" aplica a funcao resumo SHA256 sobre a chave de criptografia

		Args:
			v (int): chave de criptografia pura

		Returns:
			str: nova chave de criptografia reduzida a 128 bits
		"""
		h = sha256()
		h.update(v.to_bytes(129, "big"))
		return h.digest()[:16].hex()

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

	def __init__(self, key, iv) -> None:
		self.padding = PKCS7(block_size=256)
		self.cipher = Cipher(
			algorithm=algorithms.AES(key),
			mode=modes.CBC(iv),
			backend=default_backend()
		)
	
	def encrypt(self, msg:str) -> str:
		encryptor = self.cipher.encryptor()
		padder = self.padding.padder()
		p_msg = padder.update(msg) + padder.finalize()
		return encryptor.update(p_msg) + encryptor.finalize()

	def decrypt(self, msg:str) -> str:
		decryptor = self.cipher.decryptor()
		unpadder = self.padding.unpadder()
		p_msg = decryptor.update(bytes.fromhex(msg)) + decryptor.finalize()
		return unpadder.update(p_msg) + unpadder.finalize()


class SHA256:

	@classmethod
	def hash(self, v:int) -> int:
		h = sha256()
		h.update(str(v)[:32].encode("utf-8"))
		b = h.digest()
		return b.hex()

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
		self.iv = iv
		self.padding = PKCS7(block_size=128)
		self.cipher = Cipher(
			algorithm=algorithms.AES(key),
			mode=modes.CBC(iv),
			backend=default_backend()
		)
	
	def encrypt(self, msg:bytes) -> bytes:
		encryptor = self.cipher.encryptor()
		padder = self.padding.padder()
		p_msg = padder.update(msg) + padder.finalize()
		e_msg = encryptor.update(p_msg) + encryptor.finalize()
		return (self.iv + e_msg)

	def decrypt(self, msg:bytes) -> bytes:
		decryptor = self.cipher.decryptor()
		unpadder = self.padding.unpadder()
		p_msg = decryptor.update(msg) + decryptor.finalize()
		return unpadder.update(p_msg) + unpadder.finalize()


class SHA256:

	@classmethod
	def hash(self, v:int) -> str:
		h = sha256()
		h.update(v.to_bytes(128, "big"))
		return h.digest()[:16].hex()

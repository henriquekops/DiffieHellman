#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from sys import (
	argv,
	exit
)
from random import randint

# project dependencies
from main.diffie import DiffieHellman
from main.aes import AES
from main.state import Storage

# external dependencies
from cryptography.hazmat.primitives.hashes import SHA256
import yaml

__author__ = "Henrique Kops && Victoria Tortelli"


HELP = "python3 main.py <mode:str[exch,send,recv]> <args_path:str|msg:str>"


if __name__ == "__main__":

	if len(argv) != 2:
		print(HELP)
		exit(0)

	mode = argv[1]
	args = argv[2]

	storage = Storage()

	a, key = storage.get()

	if mode == "exch":
		if not a: a = randint(10**29, 10**30)
		data = yaml.load(args)
		diffie = DiffieHellman(a)
		v = diffie.run(data.get("p"), data.get("g"))
		key = SHA256(v[:128])
		storage.set(a, key)
	else:
		msg = args
		aes = AES(key, msg[:128])
		if mode == "recv":
			dt = aes.decrypt(msg[129:])
			print(dt)
		elif mode == "send":
			ct = aes.encrypt(msg[129:])
			print(ct)

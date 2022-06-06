#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from sys import (
	argv,
	exit
)
from random import randint
from typing import Tuple

# project dependencies
from main.diffie import DiffieHellman
from main.aes import AES
from main.state import Storage

# external dependencies
import yaml
from hashlib import sha256

__author__ = "Henrique Kops && Victoria Tortelli"


HELP = "python3 main.py <mode:str[exch,send,recv]> <args_path:str|msg:str>"


def load(args_path:str) -> Tuple[int, int]:
	f = open(args_path, "r")
	data = yaml.safe_load(f)
	f.close()
	p = int(data.get("p"), 16)
	g = int(data.get("g"), 16)
	return p, g

if __name__ == "__main__":

	if len(argv) != 3:
		print(HELP)
		exit(0)

	mode = argv[1]
	args = argv[2]

	storage = Storage()

	a, key = storage.get()

	print(f"a = {a}")
	print(f"key = {key}")

	if mode == "exch":
		if not a: a = randint(10**29, 10**30)
		else: a = int(a, 16)
		diffie = DiffieHellman(a)
		p, g = load(args)
		v = diffie.run(p, g)
		h = sha256()
		h.update(str(v)[:32].encode("utf-8"))
		key = h.digest().hex()
		print(p, '\n\n')
		print(g, '\n\n')
		print(v, '\n\n')
		print(key, '\n\n')
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

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# project dependencies
from main.state import Storage
from main.diffie import DiffieHellman
from main.crypto import (
	AES,
	SHA256
)
from main.utils import (
	MODES,
	parse_args,
	build_parser,
	gen_iv,
	load,
	check,
	invert
)


__author__ = "Henrique Kops && Victoria Tortelli"


if __name__ == "__main__":
	parser = build_parser()
	args = parse_args(parser)

	storage = Storage()

	if MODES.exch.equals(args.mode):
		p, g = load(args.argfile)
		
		if args.A:
			diffie = DiffieHellman()
			storage.set_a(diffie.a)
			A:int = diffie.run(g=g, p=p)
			print(f"A: {hex(A)[2:]}")

		else:
			a = storage.get_a()
			check(a, "a")
			diffie = DiffieHellman(a)
			V:int = diffie.run(g=int(args.key, 16), p=p)
			print(f"V: {V}")
			key:str = SHA256.hash(V)
			storage.set_key(a, key)
			print(f"key: {key}")

	elif MODES.talk.equals(args.mode):
		key = storage.get_key()
		check(key, "key")

		if args.recv is not None:
			b = bytes.fromhex(args.recv)
			iv, msg = b[:16], b[16:]
			aes = AES(key, iv)
			print(f"decrypted: {aes.decrypt(msg).decode()}")

		elif args.send is not None:	
			iv = gen_iv()
			aes = AES(key, iv)
			msg = ' '.join(args.send).encode("utf-8")
			print(f"encrypted: {aes.encrypt(msg).hex()}")

		elif args.sendinv is not None:	
			iv = gen_iv()
			aes = AES(key, iv)
			msg = ' '.join(args.sendinv).encode("utf-8")
			msg = invert(msg)
			print(f"encrypted: {aes.encrypt(msg).hex()}")

	else:
		print("Unknown mode!")

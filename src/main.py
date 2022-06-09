#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import argparse

# project dependencies
from main.state import Storage
from main.diffie import DiffieHellman
from main.crypto import (
	AES,
	SHA256
)
from main.utils import (
	MODES,
	load,
	check
)


__author__ = "Henrique Kops && Victoria Tortelli"


parser = argparse.ArgumentParser(description="DiffieHellman")
parser.add_argument("mode", help="usage mode")
subparsers = parser.add_subparsers(dest="mode", required=True)

parser_exch = subparsers.add_parser("exch", help="exchange usage mode")
group_exch = parser_exch.add_mutually_exclusive_group(required=True)
group_exch.add_argument("--key", metavar="B", type=str, help="generates key using B value")
group_exch.add_argument("--A", action="store_true", help="generates A value")
parser_exch.add_argument("--argfile", required=True, type=str, help="argument file containing public 'p' and 'g'")

parser_talk = subparsers.add_parser("talk", help="talk usage mode")
group_talk = parser_talk.add_mutually_exclusive_group(required=True)
group_talk.add_argument("--send", metavar="MSG", type=str, help="send message")
group_talk.add_argument("--recv", metavar="MSG", type=int, help="receive message")


if __name__ == "__main__":
	args = parser.parse_args()

	storage = Storage()

	if args.mode.__eq__(MODES.exch):
		p, g = load(args.argfile)
		
		if args.A:
			diffie = DiffieHellman()
			print(diffie.a)
			storage.set_a(diffie.a)
			A:int = diffie.run(g=g, p=p)
			print(A)

		else:
			a = storage.get_a()
			print(a)
			check(a, "a")
			diffie = DiffieHellman(a)
			V:int = diffie.run(g=int(args.key, 16), p=p)
			key:int = SHA256.hash(V)
			storage.set_key(a, key)
			print(key)

	else:
		msg = args
		key = storage.get_key()
		check(key, "key")
		aes = AES(key, msg[:32])

		if args.mode.__eq__(MODES.recv):
			print(aes.decrypt(msg[33:]))

		elif args.mode.__eq__(MODES.send):
			print(aes.encrypt(msg[33:]))

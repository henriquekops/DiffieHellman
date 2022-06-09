#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from typing import Tuple
from sys import exit
from enum import (
	Enum,
	auto
)
from argparse import (
	ArgumentParser,
	ArgumentError,
	ArgumentTypeError
)


# external dependencies
import yaml

__author__ = "Henrique Kops && Victoria Tortelli"


class MODES(Enum):
	exch = auto()
	talk = auto()

	def equals(self, string:str) -> bool:
		return self.name == string


def load(args_path:str) -> Tuple[int, int]:
	try:
		f = open(args_path, "r")
		try:
			data = yaml.safe_load(f)
			p = int(data.get("p"), 16)
			g = int(data.get("g"), 16)
			return p, g
		finally:
			f.close()
	except FileNotFoundError:
		print(f"File '{args_path}' not found!")
		exit(1)


def check(arg:str, argname:str) -> None:
	if not arg:
		print(f"Could not compute, '{argname}' is missing!")
		exit(1)


def parse_args(parser):
	try:
		return parser.parse_args()
	except ArgumentError or ArgumentTypeError:
		exit(1)


def build_parser() -> ArgumentParser:
	parser = ArgumentParser(description="DiffieHellman")
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
	group_talk.add_argument("--recv", metavar="MSG", type=str, help="receive message")

	return parser

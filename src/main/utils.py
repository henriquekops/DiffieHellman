#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import argparse
from random import randbytes
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
		"""valida se o modo de entrada eh conhecido por este enumerador

		Args:
			string (str): modo de entrada

		Returns:
			bool: boleano indicando se o modo eh conhecido
		"""
		return self.name == string


def load(args_path:str) -> Tuple[int, int]:
	"""carrega o numero primo e seu gerador a partir do caminho de entrada

	Args:
		args_path (str): caminho de entrada

	Returns:
		Tuple[int, int]: tupla contendo numero primo
	"""
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
	"""checa se a variavel nao eh nula

	Args:
		arg (str): variavel
		argname (str): nome da variavel para impressao
	"""
	if not arg:
		print(f"Could not compute, '{argname}' is missing!")
		exit(1)


def parse_args(parser:argparse):
	"""analisa os argumentos

	Args:
		parser (argparse): analisador

	Returns:
		_type_: dicionario contendo os argumentos de entrada
	"""
	try:
		return parser.parse_args()
	except ArgumentError or ArgumentTypeError:
		exit(1)


def gen_iv() -> bytes:
	"""gera o vetor de inicializacao

	Returns:
		bytes: o vetor de inicializacao
	"""
	return randbytes(16)


def invert(msg: str) -> str:
	"""inverte a mensagem

	Args:
		msg (str): mensagem

	Returns:
		str: mensagem invertida
	"""
	return msg[::-1]


def build_parser() -> ArgumentParser:
	"""construtor de analisador de argumentos

	Returns:
		ArgumentParser: analisador de argumentos
	"""
	parser = ArgumentParser(description="DiffieHellman")
	parser.add_argument("mode", help="usage mode")
	
	subparsers = parser.add_subparsers(dest="mode", required=True)

	parser_exch = subparsers.add_parser("exch", help="exchange usage mode")
	parser_exch.add_argument("--argfile", required=True, type=str, help="argument file containing public 'p' and 'g'")
	group_exch = parser_exch.add_mutually_exclusive_group(required=True)
	group_exch.add_argument("--key", metavar="B", type=str, help="generates key using B value")
	group_exch.add_argument("--A", action="store_true", help="generates A value")

	parser_talk = subparsers.add_parser("talk", help="talk usage mode")
	group_talk = parser_talk.add_mutually_exclusive_group(required=True)
	group_talk.add_argument("--send", metavar="MSG", nargs="+", type=str, help="send message")
	group_talk.add_argument("--sendinv", metavar="MSG", nargs="+", type=str, help="invert message")
	group_talk.add_argument("--recv", metavar="MSG", type=str, help="receive message")

	return parser

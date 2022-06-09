#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from typing import Tuple
from sys import exit
from enum import (
	Enum,
	auto
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

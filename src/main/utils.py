#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import enum
from typing import Tuple
from sys import exit


# external dependencies
import yaml

__author__ = "Henrique Kops && Victoria Tortelli"


class MODES(enum.Enum):
	exch:str = "exch"
	recv:str = "recv"
	send:str = "send"


def load(args_path:str) -> Tuple[int, int]:
	f = open(args_path, "r")
	data = yaml.safe_load(f)
	f.close()
	p = int(data.get("p"), 16)
	g = int(data.get("g"), 16)
	return p, g


def check(arg:str, argname:str) -> None:
	if not arg:
		print(f"Could not compute, {argname} is missing!")
		exit(1)

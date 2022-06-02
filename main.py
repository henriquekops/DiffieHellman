#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from sys import (
	argv, 
	exit
)
from random import randint
from math import pow

# project dependencies
from src.diffie import DiffieHellman

__author__ = "Henrique Kops"


HELP = "python3 main.py <g:int> <p:int>"

if __name__ == "__main__":

	if len(argv) !=3:
		print(HELP)
		exit(0)
	
	p = argv[1]
	g = argv[2]

	a = randint(pow(10,30),pow(10,31))

	d = DiffieHellman(a)

	print(a)

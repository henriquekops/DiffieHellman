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
from main.diffie import DiffieHellman

__author__ = "Henrique Kops"


HELP = "python3 main.py <g:int> <p:int> <mode:str>"
ENCRYPT = "encrypt"
DECRYPT = "decrypt"


if __name__ == "__main__":

	if len(argv) !=3:
		print(HELP)
		exit(0)

	p = argv[1]
	g = argv[2]
	
	a = randint(pow(10,29), pow(10,30))
	
	d = DiffieHellman(a)

	print(d.run(p, g))


# p = '''B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C6\
# 9A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C0\
# 13ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD70\
# 98488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0\
# A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708\
# DF1FB2BC2E4A4371'''

# g = '''A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507F\
# D6406CFF14266D31266FEA1E5C41564B777E690F5504F213\
# 160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1\
# 909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28A\
# D662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24\
# 855E6EEB22B3B2E5'''

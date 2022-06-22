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


# Última mensagem cifrada trocada com o professor:
# 729BD71B58F5DF7D08D7D97A5E1C483A79B67CD58A554303C397433600CC7D1E0F50333D0
# 1233B9DDB05ADEADC308450E4F1EE987620B10BB1F0F959E183566871F0140E5A6BC29B32
# 5B76E98C890FA269D20BDD9BE18B5D3BEBB768E7402F2901A6EE7C15D33DAF4D21F5AB721
# 581C6504B9412ED5FEB13842DC6D6C98DB6EA351FE2FD8BA2EF6D90502A3D07C1FE26B64A
# B81811C414644C26F649A446897880BD69D6FB3BC59EC07F1AECBAF69B4CEA220A07C3765
# 47B7FAA53A09C48D94BA3EF8DBE710281D8635C2FEF35722DA526489875147EC967649CEE
# 28A843FBA7D76B5692AD7F02F96CC55F44748F6127
#
# Mensagem decifrada:
# Agora sim. Tudo certo. Enviar o B errado faz com que a senha gerada não de
# certo :-). Bem, agora comenta bem o código incluindo este exemplo completo
# no início do código como comentário e submetam no Moodle. Valeu


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

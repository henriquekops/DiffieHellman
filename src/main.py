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
	parser = build_parser() #constroi o parser dos argumentos de entrada
	args = parse_args(parser) #analisa os argumentos de entrada e os coloca em um dicionario 

	storage = Storage() #monta uma fachada para uma camada de comunicacao para o banco de dados (sqlite) 

	if MODES.exch.equals(args.mode): #se o usuario quer trocar chaves
		p, g = load(args.argfile) #carrega o valor do numero primo e seu gerador de um arquivo de entrada (--argfile) 
		
		if args.A: #se o usuario quer gerar uma chave publica nova
			diffie = DiffieHellman() #constroi o objeto do algoritmo de troca de chaves com uma chave privada aleatoria
			storage.set_a(diffie.a) #armazena a chave privada para utiliza-la depois
			A:int = diffie.run(g=g, p=p) #executa o diffieHellman a partir do primo e seu gerador para criar a chave publica
			print(f"A: {hex(A)[2:]}") #mostra o valor da chave publica para o usuario

		else: #senao a unica outra opcao para o usuario eh gerar a chave de criptografia a partir da chave publica do remetente
			a = storage.get_a() #pega a chave privada ja criada
			check(a, "a") #verifica se a chave realmente existe
			diffie = DiffieHellman(a) #constroi o objeto do algoritmo de troca de chaves com uma chave privada ja criada
			V:int = diffie.run(g=int(args.key, 16), p=p) #executa o algoritmo de criacao de chave de criptografia a partir da chave publica recebida
			key:str = SHA256.hash(V) #realiza o SHA256 para os primeiros 128 bits da chave
			storage.set_key(a, key) #armazena a chave para usar durante a comunicacao segura
			print(f"key: {key}") #mostra a chave de criptografia para o usuario

	elif MODES.talk.equals(args.mode): #caso o usuario queira trocar mensagens
		key = storage.get_key() #busca a chave de criptografia armazenada 
		check(key, "key") #verifica se a chave existe 

		if args.recv is not None: #se o usuario quer receber uma mensagem
			b = bytes.fromhex(args.recv) #converte a chave publica do remetente para um array de bytes
			iv, msg = b[:16], b[16:] #separa o vetor de inicializacao do restante da mensagem
			aes = AES(key, iv) #constroi o objeto que armazena o algoritmo de cifragem
			print(f"decrypted: {aes.decrypt(msg).decode()}") #mostra a messagem descriptografada para o usuario
			
		elif args.send is not None:	#se o usuario quer mandar uma mensagem
			iv = gen_iv() #gera um vetor de inicializacao aleatorio
			aes = AES(key, iv) #constroi o objeto que armazena o algoritmo de cifragem 
			msg = ' '.join(args.send).encode("utf-8") #gera a mensagem com uma string codificada em utf-8
			print(f"encrypted: {aes.encrypt(msg).hex()}") #mostra a mensagem criptografada para o usuario

		elif args.sendinv is not None:	#se o usuario quer mandar uma mensagem invertida
			iv = gen_iv() #gera um vetor de inicializacao aleatorio
			aes = AES(key, iv) #constroi o objeto que armazena o algoritmo de cifragem 
			msg = ' '.join(args.sendinv).encode("utf-8") #gera a mensagem com uma string codificada em utf-8
			msg = invert(msg) #inverte a mensagem 
			print(f"encrypted: {aes.encrypt(msg).hex()}") #mostra a mensagem invertida criptografada para o usuario

	else:
		print("Unknown mode!") #caso nenhum modo escolhido pelo usuario seja valido, mostra essa mensagem

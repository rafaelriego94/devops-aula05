import jogovelha 
import SYS 

errolnicializar = False 
jogo = jogovelha.inicializar() 

if len(jogo) != 3:
	errolnicializar = True 
else: 
	for linha in jogo: 
		if len(linha) != 3: 
			errolnicializar = True 
		else: 
			for elemento in linha: 
				if elemento != '.':
					errolnicializar = True
if errolnicializar: 
	sys.exit(l) 
else:
	sys.exit(0) 
	
import random #importa o modulo random


def comp(c): #guarda variavéis para o jogo contra o computador
	tab = [[4,4,4,4,4,4], [4,4,4,4,4,4]]
	p1 = 0
	p2 = 0
	player(tab, p1, p2, c)

def player(tab, p1, p2, c):
	player1 = input('Qual é o seu nome Jogador 1?: ')
	player2 = "Computador"
	if player1 == player2: #garante que ambos os jogadores tem nomes diferentes
		print('Os nomes nao podem ser iguais, por favor escolha um nome novo')
		player(tab, p1, p2, c)
	
	pjogada(player1, player2, tab, p1, p2, c)

def jogada_comp(tab, p1, p2, player1, player2, c, f):
	
	for i in range(6):  
		if tab[1][i]==0:
				jogada = random.choice(tab[1])
		elif 1<tab[0][i]<4:
			if int(tab[0][i])/int(tab[1][i])==1: 
				jogada = i+1
			else:
				jogada = random.choice(tab[1])
		else:
			jogada= random.choice(tab[1])

	if p1<25 and p2<25:
				temp = jogada - 1 #uma vez que as listas comecam no 0 queremos que o input 1 corresponda ao elemento 0 da lista e assim sucessivamente
				tempReverse = 5 #momento da mudanca de lista, corresponde ao primeiro elemnto da lista 2
				temp_l = 0
				for i in range(tab[1][temp]):
					if (temp + 1 <= 5) :
						tab[1][temp+1] = tab[1][temp+1]+1
						temp = temp + 1
						tab[1][jogada-1] = 0
					elif temp >= 5:
						tab[0][tempReverse]=tab[0][tempReverse]+1
						tempReverse = tempReverse - 1
						tab[1][jogada-1] = 0
					elif tempReverse < 0:
						tab[1][temp_l] = tab[1][temp_l]+1
						temp_l += 1

				if tempReverse != 5:
					if 1<tab[0][tempReverse+1]<4 :
							p2 = p2 + tab[0][tempReverse+1]
							tab[0][tempReverse+1] = 0
							if 1<tab[0][tempReverse+2]<4:
									p2 = p2 + tab[0][tempReverse+2]
									tab[0][tempReverse+2] = 0
									if 1<tab[0][tempReverse+3]<4 :
										p2 = p2 + tab[0][tempReverse+3]
										tab[0][tempReverse+3] = 0
										if 1<tab[0][tempReverse+4]<4 :
											p2 = p2 + tab[0][tempReverse+4]
											tab[0][tempReverse+4] = 0
											if 1<tab[0][tempReverse+5]<4 :
												p2 = p2 + tab[0][tempReverse+5]
												tab[0][tempReverse+5] = 0
													
				 
				continua_par(tab, p1, p2, player1, player2, c, f)

	else:
		if p1>= 25:
			print("Parabéns", p1, "ganhaste!")
		elif p2>= 25:
					print("Parabéns", p2, "ganhaste!")


def continua_jogo(tab, p1, p2, player1, player2, c, f):
	if c == '1':
		continua_impar(tab, p1, p2, player1, player2, c, f)
	elif c == '3':
		jogada_comp(tab, p1, p2, player1, player2, c, f)

def jogada_par(tab, p1, p2, player1, player2, c, f):
	jogada = ""
	try: 
		#a funçao vai tentar pedir ao utilizador um numero interiro, se isto acontecer o jogo continua, senao avanca para o ValueError
		jogada = int(input('Escolhe a casa que pretendes jogar (utiliza as teclas de 1 a 6): '))
	except ValueError: #evita que o jogo seja burlando a dar erro
		print('Introduza um valor de 1 a 6: ')
		jogada_par(tab, p1, p2, player1, player2, c, f)
	else:
		if tab[0][jogada-1] == 0: #anula a hipotese de jogar numa casa com o numero zero
			print('Esta casa tem o valor zero, por isso nao esta disponivel ')
			jogada_par(tab, p1, p2, player1, player2, c, f)
		elif jogada >= 1 and jogada <= 6: 
			#verifica se o numero dado esta presente no intervalo [1,6]


			if p1<25 and p2<25:
				temp = jogada - 1 #uma vez que as listas comecam no 0 queremos que o input 1 corresponda ao elemento 0 da lista e assim sucessivamente
				tempReverse = 0 #momento da mudanca de lista, corresponde ao primeiro elemnto da lista 1
				temp_l = 5
				for i in range(tab[0][temp]): 
					if ((temp -1) >= 0) : 
						tab[0][temp-1] = tab[0][temp-1]+1 #adiciona +1 a posicao anterior a jogada
						temp = temp - 1 #atribui um novo valor a variavel temp para que o jogo possa continuar nas outras casas
						tab[0][jogada-1] = 0 #garante que a casa que o jogador escolheu fica igual a zero no fim do turno	
					elif temp <= 0: #quando (temp-1)<0 e necessario mudar de linha
						tab[1][tempReverse]= tab[1][tempReverse]+1 # adiciona +1 ao primeiro elemento da segunda linha
						tempReverse = tempReverse + 1 #atribui um novo valor a variavel tempReverse
						tab[0][jogada-1] = 0 #garante que a casa que o jogador escolheu fica igual a zero no fim do turno	
					elif tempReverse > 5:
						tab[0][temp_l] = tab[0][temp_l]+1
						temp_l -= 1
				
				if tempReverse != 0:		
					if 1<tab[1][tempReverse-1]<4 :
							p1 = p1 + tab[1][tempReverse-1]
							tab[1][tempReverse-1] = 0
							if 1<tab[1][tempReverse-2]<4:
									p1 = p1 + tab[1][tempReverse-2]
									tab[1][tempReverse-2] = 0
									if 1<tab[1][tempReverse-3]<4 :
										p1 = p1 + tab[1][tempReverse-3]
										tab[1][tempReverse-3] = 0
										if 1<tab[1][tempReverse-4]<4 :
											p1 = p1 + tab[1][tempReverse-4]
											tab[1][tempReverse-4] = 0
											if 1<tab[1][tempReverse-5]<4 :
												p1 = p1 + tab[1][tempReverse-5]
												tab[1][tempReverse-5] = 0
															
													


				continua_jogo(tab, p1, p2, player1, player2, c, f)
			else:
				if p1>= 25:
					print("Parabéns", p1, "ganhaste!")
				elif p2>= 25:
					print("Parabéns", p2, "ganhaste!")
		else:
			print('Por favor jogue uma casa valida...')
			jogada_par(tab, p1, p2, player1, player2, c, f)


def jogada_impar(tab, p1, p2, player1, player2, c, f):
	jogada = ""
	try:

		jogada = int(input('Escolhe a casa que pretendes jogar (utiliza as teclas de 1 a 6): '))
	except ValueError:
		print('Introduza um valor de 1 a 6: ')
		jogada_impar(tab, p1, p2, player1, player2, c, f)
	else:
		if tab[1][jogada-1] == 0:
			print('Esta casa tem o valor zero, por isso nao esta disponivel ')
			jogada_impar(tab, p1, p2, player1, player2, c, f)

		elif jogada >= 1 and jogada <= 6:


			if p1<25 and p2<25:
				temp = jogada - 1 #uma vez que as listas comecam no 0 queremos que o input 1 corresponda ao elemento 0 da lista e assim sucessivamente
				tempReverse = 5 #momento da mudanca de lista, corresponde ao primeiro elemnto da lista 2
				temp_l = 0
				for i in range(tab[1][temp]):
					if (temp + 1 <= 5) :
						tab[1][temp+1] = tab[1][temp+1]+1
						temp = temp + 1
						tab[1][jogada-1] = 0
					elif temp >= 5:
						tab[0][tempReverse]=tab[0][tempReverse]+1
						tempReverse = tempReverse - 1
						tab[1][jogada-1] = 0
					elif tempReverse < 0:
						tab[1][temp_l] = tab[1][temp_l]+1
						temp_l += 1


				if tempReverse != 5:
						if 1<tab[0][tempReverse+1]<4 :
							p2 = p2 + tab[0][tempReverse+1]
							tab[0][tempReverse+1] = 0
							if 1<tab[0][tempReverse+2]<4:
									p2 = p2 + tab[0][tempReverse+2]
									tab[0][tempReverse+2] = 0
									if 1<tab[0][tempReverse+3]<4 :
										p2 = p2 + tab[0][tempReverse+3]
										tab[0][tempReverse+3] = 0
										if 1<tab[0][tempReverse+4]<4 :
											p2 = p2 + tab[0][tempReverse+4]
											tab[0][tempReverse+4] = 0
											if 1<tab[0][tempReverse+5]<4 :
												p2 = p2 + tab[0][tempReverse+5]
												tab[0][tempReverse+5] = 0
																			
				 
				continua_par(tab, p1, p2, player1, player2, c, f)

			else:
				if p1>= 25:
					print("Parabéns", p1, "ganhaste!")
				elif p2>= 25:
					print("Parabéns", p2, "ganhaste!")

		else:
			print('Por favor jogue uma casa valida...')
			jogada_impar(tab, p1, p2, player1, player2, c, f)

def continua_par(tab, p1, p2, player1, player2, c, f):
	print('------------ ', player1 , p1,' ------------')
	print (tab[0][0],'  ', tab[0][1], '  ', tab[0][2], '  ', tab[0][3],'  ', tab[0][4],'  ', tab[0][5] )
	print (tab[1][0],'  ', tab[1][1], '  ', tab[1][2], '  ', tab[1][3],'  ', tab[1][4],'  ', tab[1][5] )
	print('------------ ', player2, p2,' ------------')
	print('E a tua vez de jogar', f)
	jogada_par(tab, p1, p2, player1, player2, c, f)


def continua_impar(tab, p1, p2, player1, player2, c, f):
	print('------------ ', player1 , p1,' ------------')
	print (tab[0][0],'  ', tab[0][1], '  ', tab[0][2], '  ', tab[0][3],'  ', tab[0][4],'  ', tab[0][5] )
	print (tab[1][0],'  ', tab[1][1], '  ', tab[1][2], '  ', tab[1][3],'  ', tab[1][4],'  ', tab[1][5] )
	print('------------ ', player2, p2,' ------------')
	print('E a tua vez de jogar', player2)
	if c == '1':	
		jogada_impar(tab, p1, p2, player1, player2, c, f)
	if c == '3':
		jogada_comp(tab, p1, p2, player1, player2, c, f)

def inicio_jogo(tab, p1, p2, player1, player2, c, f):
	print('------------ ', player1 , p1,' ------------')
	print (tab[0][0],'  ', tab[0][1], '  ', tab[0][2], '  ', tab[0][3],'  ', tab[0][4],'  ', tab[0][5] )
	print (tab[1][0],'  ', tab[1][1], '  ', tab[1][2], '  ', tab[1][3],'  ', tab[1][4],'  ', tab[1][5] )
	print('------------ ', player2, p2,' ------------')
	print('E a tua vez de jogar', f)
	jogada_par(tab, p1, p2, player1, player2, c, f)
	

def pjogada(player1, player2, tab, p1, p2, c):
	if c == '1':
		f = random.choice([player1, player2]) #variavel para escolher quem joga primeiro
		if f == player1: #se a escolha "aleatoria" corresponder a variavel jogador1, o jogo decorre como se nao tivesse existido uma escolha aleatoria
			inicio_jogo(tab, p1, p2, player1, player2, c, f)
		else: #caso contrario os papeis de jogador2 e jogador1 invertem-se para evitar problemas durante os turnos
			inicio_jogo(tab, p1, p2, player2, player1, c, f)
	elif c == '3':
		f = player1
		inicio_jogo(tab, p1, p2, player1, player2, c, f)
def main(c): #funcao que guarda as variaveis mais importantes
	tab = [[4,4,4,4,4,4], [4,4,4,4,4,4]]
	p1 = 0
	p2 = 0
	texto(tab, p1, p2, c)

def texto(tab, p1, p2, c):
	player1 = input('Qual é o seu nome Jogador 1?: ')
	player2 = input('Qual é o seu nome Jogador 2?: ')
	if player1 == player2: #garante que ambos os jogadores tem nomes diferentes
		print('Os nomes nao podem ser iguais, por favor escolham novos nomes')
		texto(tab, p1, p2, c)
	
	pjogada(player1, player2, tab, p1, p2, c)
	
def menu():
	print('0 - Sair')
	print('1 - Humano vs Humano: modo texto')
	print('2 - Humano vs Humano: modo gráfico (nao funciona)')
	print('3 - Humano vs Computador')
	c = input('Escolha a opção desejada: ')
	if c == '0':
		return
	if c == '1':
		print('----------------------------Bem Vindo ao Ouri!---------------------------')
		print('O objectivo do jogo é recolher mais pecas que o adversario. Vence o jogador que tiver 25 pecas ou mais.')
		print('-------------------------------------------------------------------------')
		main(c)
	if c == '3':
		print('----------------------------Bem Vindo ao Ouri!---------------------------')
		print('O objectivo do jogo é recolher mais pecas que o adversario. Vence o jogador que tiver 25 pecas ou mais.')
		print('-------------------------------------------------------------------------')
		comp(c)
	else:
		print('Opcao invalida, por favor escolha uma opcao:')
		menu()



def loop(): 
	menu()
	i = int(input())
	if (i == 0):
		return 
	return

if __name__ == "__main__":
	loop()

loop() 
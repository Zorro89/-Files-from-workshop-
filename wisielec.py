
import random
pula=['koczkodan','elektrotechnika','bławatek','foka', 'linoskoczek', 'popularny',]
slowo=random.choice(pula)


druk=('*'*len(slowo))
print('Witaj w grze "WISIELEC"! Zgadnij słowo jeśli nie chcesz zawisnąć:)')
print( 'Twoje słowo to ' + druk)
	
nietrafione_lit=[]
trafione_lit=[]
próba=0
gra=True
	
while gra:
	litera=input('Wpisz literę: ')
	if litera ==slowo:
		print('Wygrałeś!')
		break
	if litera in nietrafione_lit or litera in trafione_lit:
		print('Wpisywałeś już tą literę!')
	if litera in slowo:
		trafione_lit.append(litera)
	else:
		nietrafione_lit.append(litera)
		print('Próbuj dalej')
		próba+=1
	for i in range(len(slowo)):
		if slowo[i]==litera:
			druk=druk[:i]+slowo[i] + druk[i+1:]
	print(druk)
	
	if druk==slowo:
		play=False
		print('Gratulacje! To to słowo!:)')
		print('Spódłowałeś:'+str(próba) +'razy')
		break
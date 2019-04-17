#Vérifier si un nombre est premier
a,compt=1,0

print('Entrez un nombre : ')
numb=int(input)
while a<=numb:
	if numb%a==0:
		compt+=1
		a+=1
	else:
		a+=1
if compt==2:
	print(numb,'est un nombre premier')
else:
	print(numb,'n\'est pas un nombre premier')
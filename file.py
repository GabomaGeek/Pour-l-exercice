# Copie d'un chaine de caractere

ch,a='',0
chaine=input('Entrez un phrase : ')
while a<=len(chaine):
	ch+=chaine[a]
	a+=1
print(ch)
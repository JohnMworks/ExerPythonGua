frase = str(input('digite uma frase: ')).strip()
phrase = frase.lower()
pri = phrase.find('a')
ult = phrase.rfind('a')

print('A letra A aparece {} vezes'.format(phrase.count('a')))
print('A primeira letra A aparece na posição: {}'.format(pri))
print('A ultima letra A aparece na posição: {}'.format(ult))

print('1- Quantos albums o Mtuê tem?\na) 1\nb) 2\nc) 3\nd) 4')
p1 = input('Resposta:').lower()

if p1 not in ['a','b','c','d']:
    print('Error')
else:
    if p1 == 'a':
        print('Correct answer.')
    else:
        print('Incorrect answer.')
name = input('Whats is your name:')
yo = int(input(f'Hi ,{name}, how old are you: '))
l1 = [1,2,3,4]
l2 = [5,6,7,8,9,10,11,12,13,14]
l3 = [15,16,17,18]
l4 = [19,20,21,22,23,24,25,26,27,28,29,30]
if yo in l1:
    print('You are a baby.')
elif yo in l2:
    print('You are a child.')
elif yo in l3:
    print('You are a teenager.')
elif yo in l4:
    print('You are a adult.')
else:
    print('Incorrect wanser.')
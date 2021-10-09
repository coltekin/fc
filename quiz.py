#!/usr/bin/env python3

lat = ['iterum', 'placere', 'pergere', 'iam', 'quo?', 'igitur',
        'ducere', 'num', 'tacere', 'quis', 'ergo', 'acedere',
        'praebere', 'redere', 'aut', 'manere', 'tutus', 'eius',
        'no iam', 'incitare', 'inter', 'praestere', 'crescere', 'fere']
deu = ['wieder', 'gefallen', 'forsetzen', 'gleich', 'wohin?', 'also',
        'führen', 'etwa', 'schweigen', 'wer?', 'deshalb also',
        'sich nâhern', 'bitten', 'zurückgeben', 'oder', 'erwarten',
        'sicher', 'sein ihr',
        'nicht mehr', 'anfeuern', 'zwischen unter', 'besser sein',
        'wachsen', 'fast etwa']

correct_answers = 0
for i in range(len(lat)):
    print('Latin:', lat[i])
    answer = input('German: ')
    if answer == deu[i]:
        print('correct')
        correct_answers = correct_answers +1
    else:
        print('Wrong the correct answer is', deu[i])
print('Correct answers:', correct_answers)


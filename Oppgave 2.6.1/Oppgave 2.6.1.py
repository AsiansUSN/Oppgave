import datetime
#import math
fornavn = input('Hva er fornavnet ditt? ')
etternavn = input('Hva er etternavnet ditt? ')
age = int(input('hvor gammel er du dette året? '))
current_year = datetime.datetime.now().year
birthyear = current_year - age
year50 = birthyear + 50
print('HI', fornavn + ' ' + etternavn)
print('You are porn in', birthyear)
print('You are going to be 50 in', year50)
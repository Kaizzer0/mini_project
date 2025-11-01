print('Hello to my Quiz Game !')

as1 = 'center processing unit'
as2 = 'graphics processing unit'
as3 =  'video graphics array'
count = 0
playing = input("Do you want to play? ")
if playing.lower() != 'yes':
    quit()

answer = input('1.What is CPU mean? ')
if(answer.lower() == as1 ):
    print('that\'s correct')
    count += 1
else:
    print('wrong answer!')

answer = input('2.What is GPU mean? ')

if(answer.lower() == as2):
    print('that\'s correct')
    count +=1
else:
    print('wrong answer!')

answer = input('3.What is VGA mean? ')
if(answer.lower() == as3):
    print('that\s correct')
    count+=1
else:
    print('wrong answer')

print('You have total ' + str(count) + '/3 score')

if count == 3:
    print('You win, you so excellent like me!')
else:
    print('You LOSE :((')
done = False

while not done:
    try:
        num1= int(input('Please tell me a number''\n'))
        done = True
    except:
        print('Invalid Input , Please tell me an integer.')

done = False

while not done:
    try:
        num2= int(input('Please tell me another number''\n'))
        done=True
    except:
        print('Invalid Input , Please tell me an integer.')

import random

op_list=['+','-','*']
op= random.randint(0,2)

if op == 0:
    rhs=num1+num2

if op == 1:
    rhs=num1-num2

if op == 2:
    rhs=num1*num2

print('can you guess the missing operators(+, - or *)')
ans= input(str(num1)+' __ '+str(num2)+'='+str(rhs)+'\n')

if ans == op_list[op]:
    print('Wow, Great Job!') 
else:
    print('Pathetic 🤮')

print( )
print( )

num3 = random.randint(1,100)

op_1 = random.randint(0,2)

op_2 = random.randint(0,2)

if op_1 == 0:
    rhs= num1+num2

if op_1 == 1:
    rhs=num1-num2

if op_2 == 0:
    rhs=rhs+num3

if op_2 == 1:
    rhs= rhs-num3

print('can you guess the missing operators(++,--,-+ or +- )')
ans= input(str(num1)+' __ '+str(num2)+' __ '+ str(num3)+'='+ str(rhs)+'\n')

if ans[0] == op_list[op_1] and ans[1]== op_list[op_2]:
    print('Wow, Great Job!') 
else:
    print('Pathetic 🤮')

print(   )
print('now a looooooooong Question')

N_nums= 5
list_numbers = []
list_ops = []

for kk in range(N_nums):
    list_numbers.append(random.randint(1,100))

for kk in range(N_nums-1):
    list_ops.append(op_list[random.randint(0,1)]) 

rhs = list_numbers[0]
for kk in range(len(list_ops)):
    if list_ops[kk] == '+':
        rhs= rhs+list_numbers[kk+1]
    elif list_ops[kk]== '-':
        rhs= rhs-list_numbers[kk+1]


print('can you tell the missing operators')

qn=''

for kk in range(N_nums):
    if kk<= N_nums-2:
        qn=qn+str(list_numbers[kk])+' __ '
    else:
        qn=qn+str(list_numbers[kk])+ ' = ' +str(rhs) +'\n'

ans = input(qn)

for kk in range (N_nums-1):
    if ans[kk ] == list_ops[kk]:
        if kk== N_nums-2:
            print('GREAT JOB')
    else:
        print('Nope, Wrong!')
        break


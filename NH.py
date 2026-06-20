import random
x0 = random.randint(1,100)
y0 = random.randint(1,100)
print('I am hiding in a square region between 1,1 and 100,100. *Can you guess my position?*')
attempts = 0
Done= False

while not Done:
    guess=int(input('Guess... \n'))
    attempts = attempts+1

    if guess > n:
        print("My number is smaller than that!\n")
    
    if guess < n:
        print("My number is larger than that!\n")

    if guess == n:
        print("Bingo! You Got It!")
        print("You took ", attempts,'attempts to get it!')
        Done= True 
print( )
print( )

print('Now Your turn. Pick a number between 1 and 100')
print('Click ENTER when Ready')

input()
Done = False
attempts = 0
guess = 1
Guess_step = 10
Prevans=''
Prevans=ans
while not Done:
    ans = input('Is it '+ str(guess) + '? (l for larger,s for smaller and y for correct.)\n' )
    attempts = attempts + 1
    
    if ans == 's':
        guess = guess - Guess_step
        if guess < 1:
            guess= 1
  

    if ans == 'l':
        guess = guess + Guess_step
        if guess > 100:
            guess= 100
    

    if ans =='y':
        print('Bingo, I got it')
        print('I took ' , attempts , 'attempts to get it')
        Done=True

print()



print()
print('I will be smarter: Ima Use Binary Search')

Done = False
attempts = 0
low = 1
high = 100
guess =round(low+high)/2
while not Done:
    ans = input('Is it',+ str(guess) +'? l for larger,s for smaller and y for correct.' )
    attempts = attempts + 1
      
    if ans == 's':
        high = guess
    if ans == 'l':
        low=guess
    if ans =='y':
        print('Bingo, I got it')
        print('I took ' , attempts , 'attempts to get it')
        Done=True  


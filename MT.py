#intro
print('Hello, Welcome To The Great Anime Quiz!!!')

print('If You Win, You Will Get A Demon Slayer Corps Membership!!!')
print('If you give a single wrong answer, you lose...')
print('So, Are you ready?\n')
input()
for kk in range (1,4):
    
    print('attempt',kk)
    #Q1
    ans = input('Who is the main villan in Demon Slayer?')
    if ans.lower() == 'muzan':
        print('Yes! That is correct!!!')
        cans=1
        #Q2
        ans2=input('What is the material that Katanas in Demon Slayer are made from?')
        if ans2.lower() == 'nichirin':
            print('Yes! That is correct!!!')
            cans=cans+1
            #Q3
            ans3 = input('Now a Question about One Piece...Which Fruit did Luffy eat?')
            if ans3.lower()=='gum gum'or'rubber':
                print('Correct... You are good at this!!!')
                cans=cans+1
                #Q4
                ans4 = input("Who is Luffy's Role Model?")
                if ans4.lower() == 'shanks'or'redhead shanks':
                    print('Wow You Are Awesome!!!')
                    cans=cans+1
                    #Q5
                    ans5=input('Who taught Yuji?')
                    if ans5.lower()=='gojo':
                        print('Wow You Are Awesome!!!')
                        cans=cans+1
                        #Q6
                        ans6=input("What is Gojo's domain called?" )
                        if ans6.lower()=='infinite void':
                            print('Wow You Are Awesome!!!,you got all of them!')
                            cans=6
                        else:
                            print('You Failed...But at least You got 5')
                            cans=5
                    else:
                        print('You Failed...But at least You got 4')
                        cans=4
                else:
                    print('You Failed...But at least You got 3')
                    cans=3
            else:
                print('You Failed...But at least You got 2')
                cans=2
        else:
            print('You Failed...But at least You got 1')
            cans=1
    else:
        print('You Failed...')
        cans=0

    Done=False
    while not Done:
        if cans==6:
            print('You are a Hashira')
            print(cans)
            Done=True
        elif cans<6:
            print('You are a lower moon')
            print(cans)
            Done=True
        else:
            print('You failed Final Selection.')
            Done=True


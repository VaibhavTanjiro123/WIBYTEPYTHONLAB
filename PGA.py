print("Welcome to the Prof's office.")
print('I am his Assistant.')

print('But first you have to answer my quiz...')

ans=input('OK, Tell me what are action words called in english\n')

if ans.lower() == 'verbs':
    print('Correct, But that was just a warm up...')
else:
    print('You Are Really Very Stupid. The Prof Will Not Want To Meet You.😠')


print()

Word=input('Give me an 8 letter word with at least 3 vowels.')

if len(Word)== 8:
    print('Your Word Has 8 letters...')

    cnta=Word.count('a')
    cnte=Word.count('e')
    cnti=Word.count('i')
    cnto=Word.count('o')
    cntu=Word.count('u')
    print()
    CountVowels= cnta + cnte + cnti + cnto + cntu
    if CountVowels > 3:
        print('Wasting my time, Acting too smart.')
    elif CountVowels<3:
        print('You are trying to fool me. You gave me less than 3 vowels. I caught you.')
    else:
        print("You have no Motivation... You aren't putting any extra effort.")

else:
    print('You Are A Disaster.')

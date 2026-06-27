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

print()

sentence= input('Tell me a sentece ending in wise assistant(no questions)')

if sentence.endswith('wise assistant'):
    print('Have you not heard about puncuations? A 1st Grader can do better...')
elif sentence.endswith('wise assistant.'):
    print('OK...But wait...')
    len1st=sentence.find(' ')
    if len1st > 8:
        print('Your first word is too short...')
    elif len1st==8:
        print('Longer first word, still too short...')
    else:
        print('your first word is too long.')
else:
    print('The prof will hate you...')



print()
print('OK, pick a timing next Friday')
print('A. 18 minutes after midnight', 'B. 23 minutes past 6 AM', sep='\t\t')
print('C. 2 minutes past high noon', 'D. 2 seconds past 9 PM', sep='\t\t')
appt=input("Select a slot...(A/B/C/D) You Don't Deserve This Though...")

if appt == 'A':
    print('Beware, Prof may be sleepy')
elif appt == 'B':
    print('Careful, Prof may be jogging')
elif appt == 'C':
    print('Warning, Prof may be reading')
else:
    print('Caution, Prof may be eating dinner') 
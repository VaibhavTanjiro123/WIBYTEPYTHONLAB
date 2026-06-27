import datetime as dt
print("Welcome to the Prof's office.")
print('I am his Assistant.')

print('But first you have to answer my quiz...')
ct1=dt.datetime.now()
ans=input('OK, Tell me what are action words called in english\n')
ct2=dt.datetime.now()
diff=ct2-ct1
ans_s=ans.strip()
if ans_s.lower() == 'verbs':
    print('Correct, But that was just a warm up...')
    print('What!!!',diff.seconds,'seconds','to answer that... Very Bad')
else:
    print('You Are Really Very Stupid. The Prof Will Not Want To Meet You.😠')


print()
ct3=dt.datetime.now()
Word=input('Give me an 8 letter word with at least 3 vowels.')
ct4=dt.datetime.now()
diff=ct4-ct3
print('What!!!',diff.seconds,'seconds','to answer that... not good at all')
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
    print('You Are A Disaster. Not even 8 letters')


print()
ct5=dt.datetime.now()
sentence= input('Tell me a sentence ending in wise assistant(no question marks or exclamatory marks)')
ct6=dt.datetime.now()
diff=ct6-ct5

print('What!!!',diff.seconds,'seconds','to answer that... Really???')

if sentence.endswith('wise assistant'):
    print('Have you not heard about puncuations? A 1st Grader can do better...')
elif sentence.endswith('wise assistant.'):
    print('OK...But wait...')
    len1st=sentence.find(' ')
    if len1st > 8:
        print('Your first word is too short...')
else:
    print('The prof will hate you...')



print()
print('OK, pick a timing next Friday')
print('A. 18 minutes after midnight', 'B. 23 minutes past 6 AM', sep='\t\t')
print('C. 2 minutes past high noon', 'D. 2 seconds past 9 PM', sep='\t\t')
appt=input("Select a slot...(A/B/C/D) You Don't Deserve This Though...(ALL CAPS)")

if appt == 'A':
    print('Beware, Prof may be sleepy')
elif appt == 'B':
    print('Careful, Prof may be jogging')
elif appt == 'C':
    print('Warning, Prof may be reading')
else:
    print('Caution, Prof may be eating dinner') 
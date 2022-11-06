#Acronym project with python
# Artificial Intelligence - AI

while True:
    text = str(input('Enter your Phrase: \n')).split()
    a = ' '
    for i in text: #i = Artificial, Intelligence
        a = a + str(i[0]).upper()
    print(a)
    userWantsToQuit = input('Do you want to quit? (yes/no) \n')
    if(userWantsToQuit=='yes'):
        print('OVER')
        break


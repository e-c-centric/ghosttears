import random
from collections import Counter
  

file_dictionary= {'Countries':'countriesList.txt', 'Elements':'elementsList.txt'}
dictFile={}
c=[]
mode=input('Countries or Elements?\n').title()
with open(file_dictionary[mode], 'r') as f:
    for line in f:
        c.append(line.strip().lower())
alist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alist:
    dictFile[i]=[]
for element in c:
    for i in dictFile:
        if element.startswith(i):
            dictFile[i].append(element.title())


if __name__ == '__main__':
    print('Guess the word! CLUE: A name of a country')
      
    for i in word:
         
        print('_', end = ' ')        
    print()
  
    play = True
     
    wordGuessed = ''                
    trials = len(word) + 2
    right = 0
    flag = 0
    try:
        while (trials != 0) and flag == 0:  
            print()
            trials -= 1
  
            try:
                Guess = str(input('Guess a character and enter it: '))
            except:
                print('Only character is allowed!')
                continue
  
            
            if not Guess.isalpha():
                print('Only enter a CHARACTER')
                continue
            elif len(Guess) > 1:
                print('Please enter a SINGLE character')
                continue
            elif Guess in wordGuessed:
                print('That character has already been guessed by you!')
                continue
  
  
            
            if Guess in word:
                y = word.count(Guess) 
                for i in range(y):    
                    wordGuessed += Guess 
  
            
            for char in word:
                if char in wordGuessed and (Counter(wordGuessed) != Counter(word)):
                    print(char, end = ' ')
                    right += 1
                
                elif (Counter(wordGuessed) == Counter(word)):  
                                                                
                    print("The correct word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('WOW congrats, You won!')
                    break # To break out of the for loop
                    break # To break out of the while loop
                else:
                    print('_', end = ' ')
  
              
  
        
        if trials <= 0 and (Counter(wordGuessed) != Counter(word)):
            print()
            print('Sorry, You lost! Try again...')
            print('The correct word was {}'.format(word))
            
    if status=='GHOSTBUSTERS':
        print("Complete")
  
    except KeyboardInterrupt:
        print()
        print('Have a nice day bye! Try again..')
        exit()
import random
from datetime import datetime
trackghost_cpu='ghosttears'
trackghost_user='ghosttears'
status_ghost_user=''
status_ghost_cpu=''
status_flag_user=0
status_flag_cpu=0
dictFile={}
ghost=['g','h','o','s','t','t','e','a','r','s']
file_dictionary={
'Countries':'countriesList.txt',
'Elements':'elementsList.txt',
'Water Bodies':'water_bodies.txt'
}


def emptyvariable(x):
    x=''
    return x

def pickrandom(li,startword):
    global status_ghost_user
    global status_flag_user
    global count
    global word
    global status_ghost_cpu
    global status_flag_cpu
    
    li=[ele for ele in li if ele.startswith(startword.title())]
    
    try:
        new=random.choice(li)
        if startword.lower()==new.lower():
            word=emptyvariable(word)
            if (count%2)==0:
                status_ghost_user+=ghost[status_flag_user]
                status_flag_user+=1
            else:
                status_ghost_cpu+=ghost[status_flag_cpu]
                status_flag_cpu+=1
            count=0
                
        else:
            return new,li
        
    except:
        if not len(li):
            print('\nWord does not exist. You lose.\n')
            status_ghost_user+=ghost[status_flag_user]
            status_flag_user+=1

def addToLeaderBoard(points):
    today=datetime.today()
    with open('ghosttears_leaderboard.csv','a') as l:
        l.write(f'{today},{points}\n')

def viewLeaderBoard():
    with open('ghosttears_leaderboard.csv','r') as l:
        print('Trial          Points')
        for line in l:
            p=line.split(',')
            print(f'{p[0]}:{p[1]}')


c=[]

mode=input('Countries, Elements or Water Bodies?\n').title()

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
            
count=0
newlist=[]
word=''
state=True
while state:
    fword=input('\nEnter a word: ').lower()
    word+=fword
    if count==0:
        nList=dictFile[fword][:]
    temp=pickrandom(nList,word)
    if temp:
        aword=temp[0]
        nList=temp[1]
        c=len(aword)
        if count<=c:
            count+=1
            print('\nComputer\'s Turn...')
            word+=aword[count]
            print(word.upper(),end='\n')
            count+=1
            if word==aword.lower():
                word=emptyvariable(word)
                print('\nComputer loses\n')
                status_ghost_cpu+=ghost[status_flag_cpu]
                status_flag_cpu+=1
                print('Status ---- As it stands\n')
                print('Computer: ',end=' ')
                print((status_ghost_cpu).upper())
                print('          '+'-'*len(ghost))
                print('You     : ',end=' ')
                print((status_ghost_user).upper())
                print('          '+'-'*len(ghost))
                count=0
    else:
        word=emptyvariable(word)
        print('\nYou lose\n')
        print('Status ---- As it stands\n')
        print('Computer: ',end='')
        print((status_ghost_cpu).upper())
        print('          '+'-'*len(ghost))
        print('You     : ',end='')
        print((status_ghost_user).upper())
        print('          '+'-'*len(ghost))
        count=0
    if trackghost_cpu==status_ghost_cpu:
        print('\nComputer loses\n')
        points=10000-(1000*len(trackghost_user))
        addToLeaderBoard(points)
        if (input('Play again? Yes or No? ').lower())=='no':
            break 
    elif trackghost_user==status_ghost_user:
        print('\nYou lose\n')
        points=0
        addToLeaderBoard(points)
        if (input('Play again? Yes or No? ').lower())=='no':
            break
viewLeaderBoard()
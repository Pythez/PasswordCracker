import random
import datetime as dt
from time import sleep

def randommethod(charachters, password, size, options,start):

    tries = 0 #amount of tries it takes to find password
    attempt = []

    while True:
        for i in range(size):
            rnumber = random.randint(1, 60) #number inbetween and x,y are included
            attempt.append(charachters[rnumber-1])
        tries += 1
        strattempt = ' '.join(map(str, attempt)).replace(" ", "")
        print(strattempt, '    Tries:', tries)
        if password == strattempt:
            date = dt.datetime.now() - start
            micros = round((date.days * 24 * 60 * 60 + date.seconds) * 1000 + date.microseconds / 1000.0, 2)
            print('We guessed ', password, '   ', 'attempts: ', tries,'   ','time:', micros,'microseconds')
            # sleep(1000)
            exit()
        else: 
            attempt = []




password = str(input('What is the password?'))

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              '1','2','3','4','5','6','7','8','9'] #60 &acharacters

options = int(len(characters))
size = int(len(password))

start = dt.datetime.now()

randommethod(characters, password, size, options,start)






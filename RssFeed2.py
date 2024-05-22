import feedparser
import datetime
from termcolor import colored

# Kirjoitetaan lokiin
def kirjoita_lokiin(viesti):
    with open('loki.txt', 'a') as f:
        f.write(viesti + '\n')

# RSS-feedin url
url = 'https://www.techradar.com/fi-fi/rss/news/computing'
feed = feedparser.parse(url)

# Haetaan nykyinen viikonpäivä
day = datetime.datetime.today().weekday()

päivät = ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']
print('\n')
print(colored('********************************************************************', 'green'))
print(colored('******************* U U T I S E T **********************************', 'green'))
print(colored('********************************************************************', 'green'))

# minkä päivän uutisia haluat hakea
päivä = input('Anna päivä: ')
päivä = päivä.lower()
if päivä == 'maanantai':
     day = 0
elif päivä == 'tiistai':
     day = 1
elif päivä == 'keskiviikko':
     day = 2
elif päivä == 'torstai':
     day = 3
elif päivä == 'perjantai':
     day = 4
elif päivä == 'lauantai':
     day = 5
elif päivä == 'sunnuntai':
     day = 6

# Käydään läpi feedin uutiset

for post in feed.entries:
    # Jos uutisen päivä on sama kuin nykyinen päivä
    if post.published_parsed.tm_wday == day:
        print(colored(post.title, 'red'))
        print(colored(post.link, 'blue'))
        print('\n')
        kirjoita_lokiin(post.title + ' ' + post.link)
print('\n')
print(colored('********************************************************************', 'green'))
print(colored('******************* L O P P U **************************************', 'green'))
print(colored('********************************************************************', 'green'))
print('\n')
print('Uutiset on haettu ja tallennettu lokiin')

# Lopuksi suljetaan loki
with open('loki.txt', 'a') as f:
    f.write('Uutiset haettu: ' + str(datetime.datetime.now()) + '\n')
    f.write('********************************************************************\n')
    f.write('********************************************************************\n')
    f.write('\n')
    f.close()

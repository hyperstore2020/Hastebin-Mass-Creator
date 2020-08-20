import os
import threading

import requests

SENT = 0

def Abuse(message):
    global SENT
    r = requests.post('https://hastebin.com/documents', data=message)
    if r.status_code == 200:
        link = 'https://hastebin.com/' + r.json()['key']
        Save(message, link)
        os.system('title [Hastebin Abuse] By Dropout - Sent: %s' % (SENT))
        SENT += 1
    elif "Error adding document." in r.text:
        pass
    else:
        pass   

def Save(name, link):
    with open('Links.txt', 'a+') as f:
        f.write('Link: %s\nContent: %s\n==============\n' % (link, name))

if __name__ == "__main__":
    os.system('cls & title [Hastebin Abuse] By Dropout - Sent: %s' % (SENT))
    message = input('\033[92m>\033[0m Message\033[92m:\033[0m ')
    while True:
        for i in range(100):
            threads = threading.Thread(target=Abuse, args=(message,))
            threads.start()

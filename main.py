import os, httpx, random
from threading import Thread

webhook = input("Webhook: ")
message = input("Message: ")

proxfile1 = 'http.txt'
prox1 = list(map(lambda x:x.strip(),open(proxfile1)))

def webhookspam():
    proxy1 = random.choice(prox1)
    with httpx.Client(http2=True,proxies='http://'+proxy1) as client:
        try:
            try:
                while True:
                    response = client.post(
                        webhook,
                        json = {"content" : message},
                        params = {'wait' : True}
                    )
                    if response.status_code == 204 or response.status_code == 200:
                        print("Message sent")
                    elif response.status_code == 429:
                        print("Rate limited")
                        break
                    else:
                        pass
            except httpx.HTTPError as exc:
                pass
        except:
            pass
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        for i in range(int(20)):
            t = Thread(target=webhookspam,daemon=True).start()
            prox1 = list(map(lambda x:x.strip(),open(proxfile1)))

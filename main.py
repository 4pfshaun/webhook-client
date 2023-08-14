import os
import requests 
from colorama import Fore, init 

init(convert=True)

class WebhookClient:
    def __init__(self, url: str):
      self.url = url 
      self.headers = {
        'Content-Type': 'application/json'
      }

    def send(self, content: str):
      data = {
        'content': content
      }
      r = requests.post(
        self.url, 
        headers=self.headers,
        json=data 
      )
      if r.status_code == 404: 
        print(f"{Fore.RED}Webhook not found... closing{Fore.RESET}") 
        exit()
      if r.status_code == 429: 
        print(f"{Fore.RED}You are rate limited!!{Fore.RESET}")
      elif r.status_code == 204: 
        print(f"{Fore.GREEN}Message sent!{Fore.RESET}")

def main():
   url = input("webhook url: ") 
   client = WebhookClient(url)
   os.system("cls")
   while True: 
     message = input("message: ") 
     client.send(message)
     os.system('cls')

main()
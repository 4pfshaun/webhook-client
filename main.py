import os
import asyncio
import aiohttp
import platform  
from colorama import Fore, init 

init(convert=True)

class Client: 
    def __init__(self, url: str):
      self.url = url 
      self.headers = {
        'Content-Type': 'application/json'
      }

    async def send(self, content: str):
      """send the webhook message"""
      data = {
        'content': content
      }

      async with aiohttp.ClientSession(headers=self.headers) as session: 
        async with session.post(self.url, json=data) as r:     
          if r.status == 404: 
            print(f"{Fore.RED}[404] Webhook not found. Exiting..{Fore.RESET}")
            exit()
          
          elif r.status != 204: 
            print(f"{Fore.RED}[{r.status}] Failed to send the webhook{Fore.RESET}")      
    
    def clear(self):
      """clear the terminal"""
      if platform.uname().system == "Linux":
        os.system("clear")
      
      elif platform.uname().system == "Windows":
        os.system("cls")  
        
    async def start(self):
      """start the client"""  
      while True: 
        self.clear()
        content: str = input("Your message: ")
        await self.send(content)

async def main():
  url: str = input("Webhook url: ")
  client = Client(url)
  await client.start()

if __name__ == "__main__":
   asyncio.run(main())
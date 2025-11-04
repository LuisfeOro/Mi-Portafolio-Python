import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com" #Es un foro de hackers
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, "html.parser")

titulos = soup.select("span.titleline a")

for i, t in enumerate(titulos[:10], start = 1):
    print(f"{i}, {t.text}")
    print(f"{t["href"]}\n")
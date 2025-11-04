from pytube import Playlist

import pandas as pd


url = "https://www.youtube.com/playlist?list=PLrvCjcrXXKGYa7az6vx6bsuuhhelwNTji"

playlist = Playlist(url)

numeros = []
enlaces = []

for i, video_url in enumerate(playlist.video_urls, start = 1): #Lista de tuplas, start 1 para evitar que empiece con 0
    numeros.append(f"Video #{i}")
    enlaces.append(video_url)

df = pd.DataFrame({
    "Identificador": numeros,
    "Enlace": enlaces
})

print(df.to_string(index=False))
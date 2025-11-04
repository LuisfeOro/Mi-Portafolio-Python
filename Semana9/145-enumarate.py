from pytube import Playlist

url = "https://www.youtube.com/playlist?list=PLrvCjcrXXKGYa7az6vx6bsuuhhelwNTji"

playlist = Playlist(url)

print("LISTA DE VIDEOS EN LA PLAYLIST \n")
print(f"{"N" : <5} {"ENLACE" : <80}")
print("-"*90)

for i, video_url in enumerate(playlist.video_urls, start = 1): #Lista de tuplas, start 1 para evitar que empiece con 0
    print(f"{i: <5} - {video_url: <80}")

print("-"*90)
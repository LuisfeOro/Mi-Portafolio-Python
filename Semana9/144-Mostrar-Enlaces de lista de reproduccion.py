from pytube import Playlist

url = "https://www.youtube.com/playlist?list=PLrvCjcrXXKGYa7az6vx6bsuuhhelwNTji"

playlist = Playlist(url)

print(f"Total de videos encontrados: {len(playlist.video_urls)}\n")

for i, video_url in enumerate(playlist.video_urls, start = 1): #Lista de tuplas, start 1 para evitar que empiece con 0
    print(f"{i} - {video_url}")
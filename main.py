from pytube import YouTube

link = input("Inserta el link de YouTube: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()
video.download()
print("Descarregat!")
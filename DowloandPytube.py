from pytube import YouTube

# URL do vídeo que você deseja baixar
url = 'https://www.youtube.com/watch?v=EBCsYTcZB6c'

# Crie um objeto YouTube
yt = YouTube(url)

stream = yt.streams.get_by_itag('22')  

# Coloque a sua pasta onde irá gravar o video! 
stream.download(output_path='C:\\Users\\saturno\\Documents', filename='teste2')

print('Download concluído!')

from youtube_dl import YoutubeDL

dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=Llw9Q6akRo4'])
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
}

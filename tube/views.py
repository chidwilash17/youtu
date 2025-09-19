from django.shortcuts import render
import yt_dlp as youtube_dl

def youtube(request):
    if request.method == 'POST':
        link = request.POST['link']
        ydl_opts = {
            'format': 'bestvideo+bestaudio',
            'ffmpeg_location': r'bin',
            'outtmpl': r'C:\Users\LENOVO\Downloads\%(title)s.%(ext)s',
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            context = {'message': 'Video downloaded successfully!'}
        except Exception as e:
            context = {'message': f'Error: {str(e)}'}
        return render(request, 'youtube.html', context)
    return render(request, 'youtube.html')

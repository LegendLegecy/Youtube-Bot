from yt_dlp import YoutubeDL

def download_video(video_url):
    tries=0
    while tries <3:
        tries+=1
        try:
            options = {
                'format': 'best',  # Select the best available quality
                'outtmpl': '%(title)s.%(ext)s',  # Save with video title as filename
            }
            with YoutubeDL(options) as ydl:
                ydl.download([video_url])
            print("Download completed!")
            tries = 3
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    download_video(video_url) 

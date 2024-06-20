from pytube import Playlist, YouTube

# Replace with the actual playlist URL
URL_PLAYLIST = "Enter_url_of_playlist"
urls = []
save_file_path = 'C:\\Users\\USER\\Videos\\'


# Retrieve URLs of videos from playlist
def collect_url(URL_PLAYLIST):
    playlist = Playlist(URL_PLAYLIST)
    print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

    for url in playlist:
        urls.append(url)
        print(url, end="\n")
    # To see the retrieved URLs, uncomment the line below
    # print(urls)

# Download videos from the playlist
def download_videos():
    for url in urls:
        try:
            yt = YouTube(url)
            highest_res_stream = yt.streams.get_highest_resolution()
            highest_res_stream.download(output_path=save_file_path)
            print(f"Downloaded: {yt.title}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        
        
collect_url(URL_PLAYLIST)
download_videos()

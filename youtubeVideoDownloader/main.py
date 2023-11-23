from pytube import YouTube


def Download_Video(link:str):
    """
        This function downloads YouTube videos 

        param
        link: str (YouTube Video Link)

        output:
        video
    """
    try:
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.get_highest_resolution()
        youtube_object.download()
    except:
        print("An error has occured")
    else:
        print("Successfully Downloaded")


if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    Download_Video(link)
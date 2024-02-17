from pytube import YouTube
import os

def download_video(youtube_url, save_path=None, file_name=None):
    try:
        yt = YouTube(youtube_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if save_path:
            if not file_name:
                file_name = "video.mp4"
            video.download(output_path=save_path, filename=file_name)
            print(f"Video downloaded successfully to: {os.path.join(save_path, file_name)}")
        else:
            if not file_name:
                file_name = "video.mp4"
            video.download(filename=file_name)
            print("Video downloaded successfully.")
    except Exception as e:
        print(f"Error downloading video: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path where you want to save the video (press Enter for current directory): ").strip()
    file_name = input("Enter the file name for the video (press Enter to keep default): ").strip()

    if not save_path:
        save_path = None
    if not file_name:
        file_name = None

    download_video(video_url, save_path, file_name)

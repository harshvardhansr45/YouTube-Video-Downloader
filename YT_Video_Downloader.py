import yt_dlp

url_input = input("Enter the URL of the YouTube video: ").strip()

with yt_dlp.YoutubeDL() as ydl:
    meta = ydl.extract_info(url_input, download=False)

title = meta.get("title", "Unknown Title")
channel = meta.get("uploader", "Unknown Channel")
views = meta.get("view_count", 0)
quality = meta.get("format", "Best Available")

print(f"\nTitle: {title}")
print(f"Channel: {channel}")    
print(f"Views: {views}")    
print(f"Quality: {quality}")    

download = {
    "format": "best",
    "outtmpl": f"{title}.mp4",
    "noplaylist": True,
    "quiet": True
}

print("\nDownloading...")

with yt_dlp.YoutubeDL(download) as ydl:   
    ydl.download([url_input])

print("Download complete!")
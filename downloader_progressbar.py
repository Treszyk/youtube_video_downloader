from tkinter import ttk, messagebox
import yt_dlp
import winreg

REGISTRY_PATH = r'SOFTWARE\YoutubeDownloader'

# Function to check if URL is already downloaded
def is_downloaded(url):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REGISTRY_PATH) as key:
            # Check for the URL in the registry
            winreg.QueryValueEx(key, url)
            print('found')
            return True  # URL found, indicating it's already downloaded
    except FileNotFoundError:
        print('not found')
        return False  # URL not found, indicating it hasn't been downloaded
    
# Function to add URL to the registry after download
def add_to_registry(url, title):
    try:
        # Open or create the registry key
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, REGISTRY_PATH) as key:
            winreg.SetValueEx(key, url, 0, winreg.REG_SZ, title)  # Save the URL as a string
    except Exception as e:
        print(f"Error writing to registry: {e}")
    
class DownloaderProgressBar():
    def __init__(self, root):
        self.root = root
        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)


    def update_progress(self, d):
        if d['status'] == 'downloading':
            # Check if 'total_bytes' is available
            if 'total_bytes' in d and 'downloaded_bytes' in d:
                percent = d['downloaded_bytes'] / d['total_bytes'] * 100
                self.progress_bar['value'] = percent
                self.root.update_idletasks()

    def start_download(self, entry):
        url = entry.entry_box.get()
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL.")
            return
        
        if is_downloaded(url):
            messagebox.showinfo("Info", "This video has already been downloaded.")
            return

        self.progress_bar['value'] = 0

        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',  # Saves as title.mp4
            'progress_hooks': [self.update_progress],  # Hook to update progress
            'noplaylist': True,  # Download only a single video, not a playlist
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)  # Get video info without downloading
                title = info_dict.get('title', 'Unknown Title')
                ydl.download([url])  # Start the download

            add_to_registry(url, title)
            messagebox.showinfo("Success", "Download completed and URL saved.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
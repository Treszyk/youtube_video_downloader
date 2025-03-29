import customtkinter as ctk
from theme_manager import ThemeManager
import threading
import yt_dlp
import re
import os, sys
import subprocess
from tkinter import messagebox
from utils import BASE_DIR

class DownloadTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color='transparent')

        title = ctk.CTkLabel(self, text='YouTube Downloader', font=('Arial', 22, 'bold'))
        title.pack(pady=(10, 5))

        self.container = ctk.CTkFrame(self, fg_color='transparent')
        self.container.pack(expand=True)

        self.url_entry = ctk.CTkEntry(self.container, placeholder_text='Paste YouTube URL here...', width=400)
        self.url_entry.pack(pady=5)

        self.error_label = ctk.CTkLabel(self.container, text='', text_color=ThemeManager.get_primary_color(), font=('Arial', 12))
        self.error_label.pack(pady=(5, 0))

        self.dropdown_container = ctk.CTkFrame(self.container, fg_color='transparent')
        self.dropdown_container.pack(pady=(15, 5))

        self.quality_var = ctk.StringVar(value='4K')
        quality_label = ctk.CTkLabel(self.dropdown_container, text='Select Quality:', font=('Arial', 14), text_color=ThemeManager.get_primary_color())
        quality_label.pack(side='left', padx=(10, 5))

        self.quality_dropdown = ctk.CTkComboBox(
            self.dropdown_container, values=['4K', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p'], 
            variable=self.quality_var, fg_color=ThemeManager.get_primary_color()
        )
        self.quality_dropdown.pack(side='left', padx=(5, 10))

        self.extension_var = ctk.StringVar(value='mp4')
        extension_label = ctk.CTkLabel(self.dropdown_container, text='Select Extension:', font=('Arial', 14), text_color=ThemeManager.get_primary_color())
        extension_label.pack(side='left', padx=(10, 5))

        self.extension_dropdown = ctk.CTkComboBox(
            self.dropdown_container, values=['mp4', 'mkv', 'webm', 'avi'], 
            variable=self.extension_var, fg_color=ThemeManager.get_primary_color()
        )
        self.extension_dropdown.pack(side='left', padx=(5, 10)) 


        self.audio_var = ctk.BooleanVar()
        self.audio_checkbox = ctk.CTkCheckBox(self.container, text='Download Audio Only', variable=self.audio_var, fg_color=ThemeManager.get_primary_color())
        self.audio_checkbox.pack(pady=10)

        self.download_button = ctk.CTkButton(
            self.container, text='Start Download', 
            fg_color=ThemeManager.get_primary_color(), hover_color=ThemeManager.get_hover_color(),
            text_color='white', command=self.start_download
        )
        self.download_button.pack(pady=15)

        self.progress_bar = ctk.CTkProgressBar(self.container, width=400, progress_color=ThemeManager.get_primary_color())
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)

        self.progress_label = ctk.CTkLabel(self.container, text='0%', font=('Arial', 14), text_color=ThemeManager.get_primary_color())
        self.progress_label.pack()

        self.url_entry.bind('<KeyRelease>', self.on_key_release)

    def on_key_release(self, event):
        text = self.url_entry.get()
        if text:
            print(f"URL updated: {text}")
            if self.is_valid_url(text):
                self.error_label.configure(text='')
            else:
                self.error_label.configure(text="Invalid URL, please enter a valid YouTube URL.")

    def is_valid_url(self, url):
        youtube_url_pattern = re.compile(r'https?://(www\.)?(youtube|youtu|youtube-nocookie)\.com/.*')
        return bool(youtube_url_pattern.match(url))

    def start_download(self):
        url = self.url_entry.get()
        quality = self.quality_var.get()
        extension = self.extension_var.get()
        audio_only = self.audio_var.get()

        if not self.is_valid_url(url):
            messagebox.showerror("Invalid URL", "Please enter a valid YouTube URL.")
            return
        
        self.update_progress(0)
        self.download_complete = False
        download_thread = threading.Thread(target=self.download_video, args=(url, quality, extension, audio_only))
        download_thread.daemon = True
        download_thread.start()
    

    def convert_video(self, input_file, output_extension):
        output_file = input_file.rsplit(".", 1)[0] + f".{output_extension}" 
        if self.extension_var.get() == 'webm':
            return
        command = [
            os.path.join(BASE_DIR, 'ffmpeg.exe'),
            "-i", input_file,
            "-c:v", "copy",
            "-c:a", "aac",
            output_file       
        ]

        try:
            subprocess.run(command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            print(f"Conversion successful: {output_file}")
            os.remove(input_file)
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")

    def download_video(self, url, quality, extension, audio_only):
        print('Starting download...')
        print(f'URL: {url}')
        print(f'Quality: {quality}')
        print(f'Audio Only: {audio_only}')

        format_mapping = {
            '4K': 'bestvideo[height<=2160]+bestaudio/best',
            '1440p': 'bestvideo[height<=1440]+bestaudio/best',
            '1080p': 'bestvideo[height<=1080]+bestaudio/best',
            '720p': 'bestvideo[height<=720]+bestaudio/best',
            '480p': 'bestvideo[height<=480]+bestaudio/best',
            '360p': 'bestvideo[height<=360]+bestaudio/best',
            '240p': 'bestvideo[height<=240]+bestaudio/best',
            '144p': 'bestvideo[height<=144]+bestaudio/best',
        }

        print(BASE_DIR)
        ydl_opts = {
            "format": format_mapping[quality], 
            'outtmpl': 'downloads/%(title)s.%(ext)s', 
            'progress_hooks': [self.progress_hook], 
            'quiet': True,
            'ffmpeg_location': BASE_DIR,
        }

        if audio_only:
            ydl_opts['format'] = 'bestaudio/best' 

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict) 

            self.convert_video(file_path, extension)
            self.show_download_complete(file_path)

    def progress_hook(self, d):
        #print(d.keys())
        if d['status'] == 'downloading':
            if 'total_bytes_estimate' in d:
                progress = d['downloaded_bytes'] / d['total_bytes_estimate']
                #print(self.progress_bar.get(), progress)
                self.update_progress(progress)
            elif 'total_bytes' in d:
                progress = d['downloaded_bytes'] / d['total_bytes']
                #print(self.progress_bar.get(), progress)
                self.update_progress(progress)

    def update_progress(self, value):
        self.after(0, lambda: self.progress_bar.set(value))
        self.after(0, lambda: self.progress_label.configure(text=f'{int(value * 100)}%'))

    def show_download_complete(self, file_path):
        self.after(0, lambda: messagebox.showinfo("Download Complete", f"Download complete! File saved to:\n{file_path}"))


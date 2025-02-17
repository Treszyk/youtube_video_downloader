import customtkinter as ctk
from theme_manager import ThemeManager

class DownloadTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color='transparent')

        title = ctk.CTkLabel(self, text='YouTube Downloader', font=('Arial', 22, 'bold'))
        title.pack(pady=(10, 5))

        self.container = ctk.CTkFrame(self, fg_color='transparent')
        self.container.pack(expand=True)

        self.url_entry = ctk.CTkEntry(self.container, placeholder_text='Paste YouTube URL here...', width=400)
        self.url_entry.pack(pady=5)

        self.quality_var = ctk.StringVar(value='4K')
        quality_label = ctk.CTkLabel(self.container, text='Select Quality:', font=('Arial', 14), text_color=ThemeManager.get_primary_color())
        quality_label.pack(pady=(15, 5))

        self.quality_dropdown = ctk.CTkComboBox(
            self.container, values=['4K', '1440p', '1080p', '720p'], variable=self.quality_var, fg_color=ThemeManager.get_primary_color()
        )
        self.quality_dropdown.pack()

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

    def start_download(self):
        print('URL:', self.url_entry.get())
        print('Quality:', self.quality_var.get())
        print('Audio Only:', self.audio_var.get())

        self.update_progress(0.1)

    def update_progress(self, value):
        self.progress_bar.set(value)
        self.progress_label.configure(text=f'{int(value * 100)}%')

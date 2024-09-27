import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from input_box import InputBox
from downloader_progressbar import DownloaderProgressBar, REGISTRY_PATH
import winreg

def get_downloaded_titles():
    titles = []
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REGISTRY_PATH) as key:
            i = 0
            print(REGISTRY_PATH)
            while True:
                try:
                    url, title, numb = winreg.EnumValue(key, i)
                    print(url)
                    titles.append((url, title))  # Append (url, title) tuple
                    i += 1
                except OSError as e:
                    print('nomo')
                    break  # No more keys
    except FileNotFoundError:
        pass  # Registry path not found
    return titles

def delete_from_registry(url):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REGISTRY_PATH, 0, winreg.KEY_SET_VALUE) as key:
            winreg.DeleteValue(key, url)  # Delete the key
            print(f"Deleted {url} from registry")
    except Exception as e:
        print(f"Error deleting from registry: {e}")
class TabSwitcher:
    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(root)
        self.download_tab = ttk.Frame(self.notebook)
        self.history_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.download_tab, text='DOWNLOAD')
        self.notebook.add(self.history_tab, text='HISTORY')

        self.notebook.pack(expand=True, fill='both')
        self.create_download_tab()
        self.create_history_tab()

    def download_video(self):
        print('ab')
        self.downloader.start_download(self.entry)
        self.load_history()

    def create_download_tab(self):
        image_path = 'Youtube_logo.png'
        if image_path:
            print('a')
            img = Image.open(image_path)
            img = img.resize((250, 173))  # Resize image to fit
            self.img_tk = ImageTk.PhotoImage(img)

            # Create a label for the image and place it at the top
            img_label = tk.Label(self.download_tab, image=self.img_tk)
            img_label.pack(pady=10)

        self.entry = InputBox(self.download_tab)
        download_button = tk.Button(self.download_tab, text="DOWNLOAD", command=self.download_video, width=40, font=("Calibri 12"))
        download_button.pack(pady=10, ipady=10)
        self.downloader = DownloaderProgressBar(self.download_tab)
    
    def create_history_tab(self):
        self.history_frame = ttk.Frame(self.history_tab)
        self.history_frame.pack(padx=10, pady=10)

        # Listbox to display video titles
        self.history_listbox = tk.Listbox(self.history_frame, width=50, height=15)
        self.history_listbox.pack(side="left", fill="y", padx=(0, 10))

        # Scrollbar for the listbox
        self.scrollbar = ttk.Scrollbar(self.history_frame, orient="vertical", command=self.history_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.history_listbox.config(yscrollcommand=self.scrollbar.set)

        # Button to delete selected video
        self.delete_button = ttk.Button(self.history_frame, text="Delete Selected", command=self.delete_selected)
        self.delete_button.pack(pady=(10, 0))

        self.load_history()  # Load history when initializing

    def load_history(self):
        self.history_listbox.delete(0, tk.END)  # Clear the listbox
        downloaded_titles = get_downloaded_titles()
        for url, title in downloaded_titles:
            self.history_listbox.insert(tk.END, title)  # Insert titles into the listbox

    def delete_selected(self):
        selected_index = self.history_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a video to delete.")
            return

        title = self.history_listbox.get(selected_index)
        # Find the corresponding URL in the registry
        downloaded_titles = get_downloaded_titles()
        url_to_delete = None
        for url, title_name in downloaded_titles:
            if title_name == title:
                url_to_delete = url
                break

        if url_to_delete:
            delete_from_registry(url_to_delete)
            self.load_history()  # Reload history after deletion
            messagebox.showinfo("Success", f"Deleted '{title}' from history.")
        else:
            messagebox.showerror("Error", "Failed to find URL in registry.")


import customtkinter as ctk
from sidebar import Sidebar
from tabs.tab_manager import TabManager
from titlebar import TitleBar 

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Youtube Video Downloader")
        self.geometry("900x550")
        self.minsize(800, 500)

        self.grid_columnconfigure(1, weight=1) 
        self.grid_rowconfigure(1, weight=1) 

        self.sidebar = Sidebar(self, self.on_tab_selected)
        self.sidebar.grid(row=1, column=0, sticky="ns", padx=10, pady=10)

        self.tab_manager = TabManager(self, ctk.set_default_color_theme)
        self.tab_manager.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        self.on_tab_selected(0)  

    def on_tab_selected(self, index):
        self.tab_manager.show_tab(index)
        self.sidebar.highlight_button(index)

    def change_theme(self, color):
        self.configure(fg_color=color)
        self.sidebar.configure(fg_color=color)
        self.tab_manager.configure(fg_color=color)

    def close_window(self):
        self.destroy()

    def minimize_window(self):
        self.iconify()

    def maximize_window(self):
        self.title_bar.maximize_window()

if __name__ == "__main__":
    app = App()
    app.mainloop()

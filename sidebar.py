import customtkinter as ctk
from theme_manager import ThemeManager

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, callback):
        super().__init__(parent, width=200, corner_radius=15, fg_color='#1e1e1e')
        self.callback = callback

        self.sidebar_title = ctk.CTkLabel(self, text='Navigation', font=('Arial', 20, 'bold'))
        self.sidebar_title.pack(pady=20)

        self.tabs = ['Downloader', 'History', 'Settings']
        self.tab_buttons = []
        for i, tab in enumerate(self.tabs):
            button = ctk.CTkButton(
                self, text=tab, 
                command=lambda i=i: self.callback(i),
                fg_color='#292929', hover_color=ThemeManager.get_hover_color(),
                corner_radius=10, height=40
            )
            button.pack(fill='x', padx=15, pady=5)
            self.tab_buttons.append(button)

    def highlight_button(self, index):
        for i, button in enumerate(self.tab_buttons):
            if i == index:
                button.configure(fg_color=ThemeManager.get_primary_color())  # Active
                #button.configure(text_color='black')
            else:
                button.configure(fg_color='#292929')  # Inactive
                #button.configure(text_color='white')

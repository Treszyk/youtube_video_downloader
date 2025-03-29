import customtkinter as ctk
from theme_manager import ThemeManager
from tkinter import messagebox
from modals.custom_msgbox import CustomDialogBox
from modals.custom_infobox import CustomInfoBox
import os

class SettingsTab(ctk.CTkFrame):
    def __init__(self, parent, reset_callback):
        super().__init__(parent, fg_color='transparent')
        self.reset_callback = reset_callback

        title = ctk.CTkLabel(self, text='Settings', font=('Arial', 22, 'bold'))
        title.pack(pady=(10, 5))

        theme_label = ctk.CTkLabel(self, text='Select Theme Color:', font=('Arial', 14))
        theme_label.pack(pady=(20, 5))

        self.theme_var = ctk.StringVar(value=ThemeManager.current_theme)
        self.theme_dropdown = ctk.CTkComboBox(
            self, values=list(ThemeManager.color_presets.keys()), variable=self.theme_var, command=self.change_theme
        )
        self.theme_dropdown.pack()

        self.clear_cache_button = ctk.CTkButton(self, text='Clear Cache', command=self.clear_cache,
                fg_color=ThemeManager.get_primary_color(), hover_color=ThemeManager.get_hover_color()
        )
        self.clear_cache_button.pack(pady=(20, 5))

    def change_theme(self, selected_theme):
        ThemeManager.set_colors(selected_theme)
        self.reset_callback()

    def clear_cache(self):
        settings_file = 'settings.json'
        cache_files = [settings_file] 
        dialog = CustomDialogBox(self.master.master, title="Clear Cache", message="Are you sure you want to clear the cache?", confirm_callback=self.clear_cache)
        response = dialog.wait_for_response()
        if response:
            for file in cache_files:
                if os.path.exists(file):
                    try:
                        os.remove(file)
                        print(f'Cache file {file} has been cleared.')
                    except Exception as e:
                        print(f'Error deleting {file}: {e}')
                else:
                    print(f'{file} does not exist.')
            CustomInfoBox(self.master.master, 'Cache Cleared', 'Cache files have been cleared successfully.')
            self.reset_callback()
        else:
            print('Cache clearing cancelled.')

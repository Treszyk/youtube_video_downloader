import customtkinter as ctk
from tabs.download_tab import DownloadTab
from tabs.settings_tab import SettingsTab
from tabs.history_tab import HistoryTab

class TabManager(ctk.CTkFrame):
    def __init__(self, parent, reset_callback):
        super().__init__(parent, fg_color='#252525')
        self.reset_callback = reset_callback

        self.tabs = [
            DownloadTab(self),
            HistoryTab(self),
            SettingsTab(self, reset_callback),
        ]

        for tab in self.tabs:
            tab.pack_forget()

    def show_tab(self, index):
        for frame in self.tabs:
            frame.pack_forget() 

        tab_to_show = self.tabs[index]
        tab_to_show.pack(fill='both', expand=True)

        self.fade_in(tab_to_show)

    def fade_in(self, frame, color='#353535', steps=20, delay=10, current_step=0):
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        
        start_color = '#1f1f1f'
        sr, sg, sb = int(start_color[1:3], 16), int(start_color[3:5], 16), int(start_color[5:7], 16)
        
        r_step = (r - sr) / steps
        g_step = (g - sg) / steps
        b_step = (b - sb) / steps

        current_r = int(sr + r_step * current_step)
        current_g = int(sg + g_step * current_step)
        current_b = int(sb + b_step * current_step)
        
        color_to_set = f'#{current_r:02x}{current_g:02x}{current_b:02x}'

        frame.configure(fg_color=color_to_set)

        if current_step < steps:
              self.master.after_task_ids.append(self.after(delay, self.fade_in, frame, color, steps, delay, current_step + 1))

import customtkinter as ctk

#currently unused custom TitleBar
class TitleBar(ctk.CTkFrame):
    def __init__(self, parent, close_command, minimize_command, maximize_command):
        super().__init__(parent, height=40, fg_color='#333333')
        
        self.close_command = close_command
        self.minimize_command = minimize_command
        self.maximize_command = maximize_command
        

        self.title_label = ctk.CTkLabel(self, text='Youtube Video Downloader', font=('Arial', 14, 'bold'))
        self.title_label.pack(side='left', padx=15, pady=5)

        self.close_button = ctk.CTkButton(self, text='X', width=40, height=40, command=self.close_window,
                                          fg_color='transparent', text_color='white', hover_color='#444444', border_width=0)
        self.close_button.pack(side='right', padx=0, pady=0, fill='y')

        self.title_bar = self
        self.title_bar.bind('<B1-Motion>', self.drag_window)
        self.title_bar.bind('<ButtonRelease-1>', self.release_window)
        
        self.dragging = False
        self.is_maximized = False
    
    def close_window(self):
        self.close_command()

    def drag_window(self, event):
        if not self.dragging:
            self.dragging = True
            self.x_offset = event.x
            self.y_offset = event.y
        self.master.geometry(f'+{self.master.winfo_x() + event.x - self.x_offset}+{self.master.winfo_y() + event.y - self.y_offset}')

    def release_window(self, event):
        self.dragging = False

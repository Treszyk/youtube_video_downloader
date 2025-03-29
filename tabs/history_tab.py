import customtkinter as ctk

class HistoryTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text='History Page', font=('Arial', 24, 'bold'))
        label.pack(pady=20)

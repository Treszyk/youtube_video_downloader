import customtkinter as ctk

class DashboardTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Welcome to Dashboard", font=("Arial", 24, "bold"))
        label.pack(pady=20)

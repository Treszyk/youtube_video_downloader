import customtkinter as ctk
from theme_manager import ThemeManager
class CustomDialogBox(ctk.CTkToplevel):
    def __init__(self, parent, title="Confirm", message="Do you want to clear the cache?", confirm_callback=None):
        super().__init__(parent)

        self.title(title)
        self.geometry("350x180")
        self.resizable(False, False)

        self.grab_set()
        self.after(200, lambda: self.iconbitmap("static/icon.ico"))
        self.confirm_callback = confirm_callback

        self.response = False

        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        modal_width = self.winfo_width()
        modal_height = self.winfo_height()

        x_position = (parent_width - modal_width) // 2
        y_position = (parent_height - modal_height) // 2

        self.geometry(f"+{x_position + parent.winfo_x()}+{y_position + parent.winfo_y()}")
        frame = ctk.CTkFrame(self, width=330, height=130, fg_color='transparent')
        frame.pack(pady=10, padx=10, fill="both", expand=True)
        frame.pack_propagate(False) 

        self.label = ctk.CTkLabel(frame, text=message, wraplength=300, anchor="center", justify="center")
        self.label.pack(pady=(15, 20), padx=10)

        button_frame = ctk.CTkFrame(frame, fg_color='transparent')
        button_frame.pack(pady=5)

        self.yes_button = ctk.CTkButton(button_frame, text="Yes", fg_color='#292929', hover_color=ThemeManager.get_primary_color(), command=self.yes)
        self.yes_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.no_button = ctk.CTkButton(button_frame, text="No", fg_color='#292929', hover_color=ThemeManager.get_primary_color(), command=self.no)
        self.no_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

    def yes(self):
        self.response = True
        self.destroy()

    def no(self):
        self.response = False
        self.destroy()

    def wait_for_response(self):
        self.wait_window(self)
        return self.response

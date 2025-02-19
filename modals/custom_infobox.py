import customtkinter as ctk
from theme_manager import ThemeManager

class CustomInfoBox(ctk.CTkToplevel):
    def __init__(self, parent, title="Info", message="Operation completed successfully"):
        super().__init__(parent)

        self.title(title)
        self.geometry("350x180")
        self.resizable(False, False)

        self.grab_set()
        self.after(200, lambda: self.iconbitmap("static/icon.ico"))

        self.response = False
        
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        modal_width = self.winfo_width()
        modal_height = self.winfo_height()

        x_position = (parent_width - modal_width) // 2
        y_position = (parent_height - modal_height) // 2

        self.geometry(f"+{x_position + parent.winfo_x()}+{y_position + parent.winfo_y()}")

        frame = ctk.CTkFrame(self, width=330, height=100, fg_color='transparent')
        frame.pack(pady=10, padx=10, fill="both", expand=True)
        frame.pack_propagate(False)

        self.label = ctk.CTkLabel(frame, text=message, wraplength=300, anchor="center", justify="center")
        self.label.grid(row=0, column=0, padx=10, pady=(15, 20), sticky="nsew")

        button_frame = ctk.CTkFrame(frame, fg_color='transparent')
        button_frame.grid(row=1, column=0, pady=5, sticky="ew")

        self.ok_button = ctk.CTkButton(
            button_frame, 
            text="OK", 
            fg_color='#292929', 
            hover_color=ThemeManager.get_primary_color(), 
            command=self.ok
        )
        self.ok_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        button_frame.grid_columnconfigure(0, weight=1)
        self.show_info()

    def ok(self):
        self.response = True
        self.destroy()

    def show_info(self):
        self.wait_window(self)
        return self.response

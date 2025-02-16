import customtkinter as ctk

class SettingsTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Settings Page", font=("Arial", 24, "bold"))
        label.pack(pady=20)

        # Window size settings (width and height)
        self.width_label = ctk.CTkLabel(self, text="Window Width:")
        self.width_label.pack(pady=5)

        self.width_entry = ctk.CTkEntry(self, width=200)
        self.width_entry.pack(pady=5)
        self.width_entry.insert(0, "900")  # Default width

        self.height_label = ctk.CTkLabel(self, text="Window Height:")
        self.height_label.pack(pady=5)

        self.height_entry = ctk.CTkEntry(self, width=200)
        self.height_entry.pack(pady=5)
        self.height_entry.insert(0, "550")  # Default height

        # Fullscreen checkbox
        self.fullscreen_var = ctk.IntVar(value=0)  # Default: not fullscreen
        self.fullscreen_checkbox = ctk.CTkCheckBox(self, text="Fullscreen", variable=self.fullscreen_var)
        self.fullscreen_checkbox.pack(pady=10)

        self.apply_button = ctk.CTkButton(self, text="Apply", command=self.apply_settings)
        self.apply_button.pack(pady=20)

    def apply_settings(self):
        """Apply the window size or fullscreen setting."""
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())

        if self.fullscreen_var.get() == 1:
            self.master.master.attributes('-fullscreen', True)  # Set to fullscreen
        else:
            self.master.master.attributes('-fullscreen', False)  # Disable fullscreen

        self.master.master.geometry(f"{width}x{height}")
        self.master.master._windows_set_titlebar_color(self._get_appearance_mode())

import customtkinter as ctk
from sidebar import Sidebar
from tabs.tab_manager import TabManager
from theme_manager import ThemeManager

ctk.set_appearance_mode('dark')  
ctk.set_default_color_theme('blue')  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_widget_scaling(1.2)
        self.after_task_ids = []
        self.title('Youtube Video Downloader')
        self.geometry('900x550')
        self.minsize(900, 550)
        self.maxsize(900, 550)
        self.resizable(False, False)
        self.iconbitmap('static/icon.ico', default='static/icon.ico') 
        self.init_widgets()

    def init_widgets(self, curr_tab = 0):
        ThemeManager.load_theme()
        
        self.grid_columnconfigure(1, weight=1) 
        self.grid_rowconfigure(1, weight=1) 

        self.sidebar = Sidebar(self, self.on_tab_selected)
        self.sidebar.grid(row=1, column=0, sticky='ns', padx=10, pady=10)

        self.tab_manager = TabManager(self, self.reset_app)
        self.tab_manager.grid(row=1, column=1, sticky='nswe', padx=10, pady=10)

        self.on_tab_selected(curr_tab)  
    
    def clear_widgets(self):
        for widget in self.winfo_children():
            if widget.winfo_exists():
                try:
                    widget.destroy()
                except Exception as e:
                    print(f'Error destroying widget: {e}')
                    #traceback.print_exc()

    def on_tab_selected(self, index):
        self.tab_manager.show_tab(index)
        self.sidebar.highlight_button(index)

    def reset_app(self):
        for task_id in self.after_task_ids:
            #print(task_id)
            self.after_cancel(task_id)
        self.after(0, self.clear_widgets)

        self.after(10, self.init_widgets, 2)

if __name__ == '__main__':
    app = App()
    app.mainloop()

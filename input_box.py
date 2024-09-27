import tkinter as tk

class InputBox:
    def __init__(self, root):
        self.root = root
        self.entry_box = tk.Entry(root, width=40, font=("Calibri 12"))
        self.entry_box.insert(0, 'enter video URL')
        self.entry_box.config(fg='grey')
        self.entry_box.bind('<FocusIn>', self.on_entry_box_click)
        self.entry_box.bind('<FocusOut>', self.on_focusout)
        self.entry_box.pack(pady=10, ipady=10)
    
    def on_entry_box_click(self, e):
        if self.entry_box.get() == 'enter video URL':
            self.entry_box.delete(0, "end")  # delete all the text in the entry_box
            self.entry_box.insert(0, '')  # insert blank for user input
            self.entry_box.config(fg='black')

    def on_focusout(self, e):
        if self.entry_box.get() == '':
            self.entry_box.insert(0, 'enter video URL')
            self.entry_box.config(fg='grey')
import tkinter as tk

class InputBox:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root, width=40, font=("Calibri 12"))
        self.entry.insert(0, 'enter video URL')
        self.entry.config(fg='grey')
        self.entry.bind('<FocusIn>', self.on_entry_click)
        self.entry.bind('<FocusOut>', self.on_focusout)
        self.entry.pack(pady=10, ipady=10)
    
    def on_entry_click(self, e):
        if self.entry.get() == 'enter video URL':
            self.entry.delete(0, "end")  # delete all the text in the entry
            self.entry.insert(0, '')  # insert blank for user input
            self.entry.config(fg='black')

    def on_focusout(self, e):
        if self.entry.get() == '':
            self.entry.insert(0, 'enter video URL')
            self.entry.config(fg='grey')
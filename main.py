import tkinter as tk
from input_box import InputBox
from PIL import Image, ImageTk

def load_image(image_path, root):
    if image_path:
        img = Image.open(image_path)
        img = img.resize((300, 150))  # Resize image to fit
        img_tk = ImageTk.PhotoImage(img)

        # Create a label for the image and place it at the top
        img_label = tk.Label(root, image=img_tk)
        img_label.pack(pady=10)

def download_video():
    pass
if __name__=='__main__':
    app = tk.Tk()
    app.resizable(0,0)
    app.iconbitmap("Youtube_logo.ico")
    app.title('Youtube Video Downloader')
    #app.config(bg="#26242f")   
    app.geometry("400x400")
    app.minsize(450, 350)
    app.maxsize(450, 350)
    image_path = 'Youtube_logo.png'
    if image_path:
        img = Image.open(image_path)
        img = img.resize((250, 173))  # Resize image to fit
        img_tk = ImageTk.PhotoImage(img)

        # Create a label for the image and place it at the top
        img_label = tk.Label(app, image=img_tk)
        img_label.pack(pady=10)
    entry = InputBox(app)
    download_button = tk.Button(app, text="DOWNLOAD", command=download_video, width=40, font=("Calibri 12"))
    download_button.pack(pady=10, ipady=10)
    app.mainloop()
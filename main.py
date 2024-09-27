import tkinter as tk
from input_box import InputBox
from PIL import Image, ImageTk
from tab_switcher import TabSwitcher

def load_image(image_path, root):
    if image_path:
        img = Image.open(image_path)
        img = img.resize((300, 150))  # Resize image to fit
        img_tk = ImageTk.PhotoImage(img)

        # Create a label for the image and place it at the top
        img_label = tk.Label(root, image=img_tk)
        img_label.pack(pady=10)


if __name__=='__main__':
    app = tk.Tk()
    app.resizable(0,0)
    app.iconbitmap("Youtube_logo.ico")
    app.title('Youtube Video Downloader')
    app.geometry("400x400")
    app.minsize(450, 400)
    app.maxsize(450, 400)
    #app.config(bg="#26242f")   

    switcher = TabSwitcher(app)



    app.mainloop()
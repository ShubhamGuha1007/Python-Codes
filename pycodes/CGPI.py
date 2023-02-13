import qrcode
import tkinter as tk
from PIL import Image, ImageTk

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def display_qr_code(url):
    img = generate_qr_code(url)
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img

def main():
    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("300x400")

    label = tk.Label(root, text="Enter URL:")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    button = tk.Button(root, text="Generate QR Code", command=lambda: display_qr_code(entry.get()))
    button.pack()

    label = tk.Label(root)
    label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

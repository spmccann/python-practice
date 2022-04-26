from tkinter import ttk, filedialog, simpledialog, Tk, Button
from PIL import Image, ImageDraw, ImageFont

window = Tk()
frm = ttk.Frame(window, padding=20)
frm.grid()


def upload_image():
    file = filedialog.askopenfilename(title="Select Image")
    # get an image
    with Image.open(rf"{file}").convert("RGBA") as base:
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype("watermark/fonts/amatic/AmaticSC-Regular.ttf", 200)
        d = ImageDraw.Draw(txt)
        value = simpledialog.askstring("Input", "Enter Watermark text: ")
        d.text((10, 10), value, font=fnt, fill=(255, 255, 255, 128))
        out = Image.alpha_composite(base, txt)
        out.show()


Button(frm, text="Upload", command=upload_image).grid(column=1, row=1)

window.mainloop()

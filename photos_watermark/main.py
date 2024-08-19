from tkinter import *
from tkinter.simpledialog import askstring

from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter import filedialog
import os
def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename


class WatermarkProperties:
    def __init__(self):
        self.size = 0.1
        self.opacity = 0.2
        self.rotation = 10 # TODO:
        self.logo_count = 1


class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("675x140+400+150")
        self.title('Watermark Image')
        self.resizable(width=True, height=True)
        # self.configure(background='white')

        self.create_widgets()

    def save_image(self):
        new_file_name = "picture" + ".png"
        imgpil = ImageTk.getimage(self.img_label.image)
        imgpil.save(os.path.join("", new_file_name), "PNG")
        imgpil.close()

    def calculate_proportion(self, img):
        window_width = 1000
        window_height = 700
        proportion = min(window_width / img.width, window_height / img.height)
        new_width = int(img.width * proportion) - 15
        new_height = int(img.height * proportion) - 120
        self.geometry(f"{new_width + 15}x{new_height + 170}+200+30")
        return new_width, new_height

    def add_text(self, font_size=24, color="white"):
        watermark_text = askstring("Watermark", "Input text:")

        img = ImageTk.getimage(self.main_img)
        width, height = img.size

        font = ImageFont.truetype('arial.ttf', font_size)
        # font = ImageFont.load_default(size=24)

        draw = ImageDraw.Draw(img)

        x_position = width - 200
        y_position = height - 50

        draw.text((x_position, y_position), watermark_text, fill=color, font=font)

        self.main_img = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.main_img)
        self.img_label.image = self.main_img

    def modify_opacity(self, value):
        #for watermark in self.watermark_list:
        self.main_image_copy = self.main_img
        self.logo_image.putalpha(int(float(value)*255))
        # watermark.putalpha(int(float(value)*255))
        self.add_img_watermark(4)

    def modify_logo_size(self, value):
        #for watermark in self.watermark_list:
        self.main_image_copy = self.main_img

        logo_width, logo_height = self.logo_size
        new_logo_width = int(float(float(logo_width) * float(value)))
        new_logo_height = int(float(float(logo_width) * float(value)))
        self.logo_image = self.logo_image.resize((new_logo_width, new_logo_height), Image.Resampling.LANCZOS)
        try:
            self.add_img_watermark(4)
        except:
            pass

    def modify_rotation(self, param):
        self.main_image_copy = self.main_img
        self.logo_image.rotate(int(param), expand=True, resample=Image.Resampling.NEAREST)
        self.add_img_watermark(4)

    def create_logo_properties(self):
        watermark_props = WatermarkProperties()

        size_label = Label(self.frame, text="Size:", font=("Helvetica", 12))
        size_scale = Scale(self.frame, from_=0.01, to=1.0, resolution=0.02, orient="horizontal",
                           variable=watermark_props.size, command=self.modify_logo_size)
        size_scale.set(watermark_props.size)

        opacity_label = Label(self.frame, text="Opacity:", font=("Helvetica", 12))
        self.opacity_scale = Scale(self.frame, from_=0.1, to=1.0, resolution=0.1, orient="horizontal",
                              variable=watermark_props.opacity, command=self.modify_opacity)

        rotation_label = Label(self.frame, text="Rotation (degrees):", font=("Helvetica", 12))
        rotation_scale = Scale(self.frame, from_=-180, to=180, resolution=1, orient="horizontal",
                               variable=watermark_props.rotation, command=self.modify_rotation)
        rotation_scale.set(watermark_props.rotation)

        size_label.grid(row=3, column=1, columnspan=1, padx=3, pady=0)
        size_scale.grid(row=4, column=1, columnspan=1, padx=3, pady=1)
        opacity_label.grid(row=3, column=2, columnspan=1, padx=3, pady=0)
        self.opacity_scale.grid(row=4, column=2, columnspan=1, padx=3, pady=1)
        rotation_label.grid(row=3, column=3, columnspan=1, padx=3, pady=0)
        rotation_scale.grid(row=4, column=3, columnspan=1, padx=3, pady=1)

    def load_logo(self):
        watermark_props = WatermarkProperties()
        logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
        if logo_path:
            self.logo_image = Image.open(logo_path)
            logo_width, logo_height = self.logo_image.size
            self.logo_image_copy = self.logo_image
            self.logo_size = logo_width, logo_height

            self.modify_logo_size(watermark_props.size)

            self.modify_opacity(watermark_props.opacity)
            self.logo_image.rotate(watermark_props.rotation, expand=True, resample=Image.Resampling.NEAREST)
            self.modify_rotation(watermark_props.rotation)

    def load_image(self):
        # img_label.config(image=None)
        # img_label.image = None
        x = openfn()
        self.main_img = Image.open(x)
        self.main_img = self.main_img.resize(self.calculate_proportion(self.main_img), Image.Resampling.LANCZOS)
        self.main_img = ImageTk.PhotoImage(self.main_img)
        self.img_label.config(image=self.main_img)
        self.img_label.image = self.main_img

        self.add_text_button = Button(self.frame, text="Add text", command=self.add_text, height=1, width=15,
                                      font=("Helvetica", 12, "bold"), bg="#0074D9", fg="white")
        self.add_logo_button = Button(self.frame, text="Add logo", command=self.add_logo, height=1, width=15,
                                      font=("Helvetica", 12, "bold"), bg="#0074D9", fg="white")
        self.add_save_button = Button(self.frame, text="Save", command=self.save_image, height=1, width=15,
                                      font=("Helvetica", 12, "bold"), bg="#0074D9", fg="white")

        self.add_text_button.grid(row=0, column=0, columnspan=2, padx=10, pady=3)
        self.add_logo_button.grid(row=0, column=3, columnspan=2, padx=10, pady=3)
        self.add_save_button.grid(row=0, column=5, columnspan=2, padx=10, pady=3)

    def add_img_watermark(self, count=1):
        img = ImageTk.getimage(self.main_img)
        width, height = img.size
        x_spacing = width // count + 20
        y_spacing = height // count + 20

        self.logo_image.convert("RGBA")
        self.logo_image.rotate(270)

        for i in range(count):
            for j in range(count):
                x_position = i * x_spacing
                y_position = j * y_spacing
                img.paste(self.logo_image, (x_position, y_position), self.logo_image)

        self.main_image_copy = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.main_image_copy)
        self.img_label.image = self.main_image_copy

    def add_logo(self):
        self.load_logo()
        self.create_logo_properties()

        self.main_image_copy = self.main_img

        self.add_img_watermark(count=4)

    def create_widgets(self):
        self.frame = Frame(self)
        self.frame.grid(row=0, column=0, columnspan=5)
        self.frame.grid(row=1, column=0, columnspan=5)
        self.frame.grid(row=2, column=0, columnspan=3)
        self.frame.grid(row=3, column=0, columnspan=1)
        self.frame.grid(row=4, column=0, columnspan=1)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)
        self.frame.columnconfigure(5, weight=1)

        self.img_label = Label(self.frame)
        self.load_image_button = Button(self.frame, text='Load Image', command=self.load_image, height=1, width=15,
                                        font=("Helvetica", 12, "bold"), bg="#0074D9", fg="white")

        self.img_label.grid(row=1, column=1, columnspan=5, padx=3, pady=3)
        self.load_image_button.grid(row=0, column=1, columnspan=3, padx=250, pady=3)


if __name__ == "__main__":
    app = App()
    app.mainloop()

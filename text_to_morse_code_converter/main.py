import pandas
import tkinter as tk
from tkinter.font import Font
import winsound
import threading


class MorseCodeApp:
    def __init__(self, root):
        self.morse_code = ['-.-.-']  # Start signal
        self.root = root
        self.root.title("Morse Code Converter")
        self.icon_on = tk.PhotoImage(file="icon-on.png")
        self.icon_off = tk.PhotoImage(file="icon-off.png")
        self.background_image = tk.PhotoImage(file="logo.png")
        self.text_font = Font(family="Roboto", size=12, weight="bold")
        self.state = True
        self.data = pandas.read_csv("morse_code.csv", engine="python", encoding='utf-8')
        self.morse_dictionary = {row.sign: row.code for (index, row) in self.data.iterrows()}
        self.pitch = tk.IntVar(value=1000)

        self.create_gui()
        self.sound_effect()

    def create_gui(self):
        canvas = tk.Canvas(root, width=780, height=500)
        canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        canvas.pack()

        self.input_entry = tk.Text(root, width=32, height=17, font=self.text_font)
        self.input_entry.place(x=50, y=100)

        self.result_text = tk.Text(root, width=32, height=17, state="disabled", font=self.text_font)
        self.result_text.place(x=460, y=100)

        self.submit_button = tk.Button(root, text="Convert", command=self.submit_action, height=3, width=8,
                                       font=self.text_font)
        self.submit_button.place(x=360, y=190)

        self.toggle_button = tk.Button(root, image=self.icon_on, command=self.toggle_icon, height=60, width=85)
        self.toggle_button.place(x=360, y=280)

    def submit_action(self):

        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        input_data = self.input_entry.get("1.0", "end-1c")
        input_words = input_data.upper()
        try:
            self.morse_code = [self.morse_dictionary[k] for k in input_words]
        except KeyError:
            self.morse_code = '.........'
        self.result_text.insert(tk.END, f"{self.morse_code}")
        self.result_text.config(state="disabled")
        self.sound_effect()

    def toggle_icon(self):
        if self.state:
            self.toggle_button.config(image=self.icon_off)
        else:
            self.toggle_button.config(image=self.icon_on)
        self.state = not self.state

    def sound_effect(self):
        if self.state:
            for sequence in self.morse_code:
                for symbol in sequence:
                    if symbol == '.':
                        self.play_beep(200)
                    elif symbol == '-':
                        self.play_beep(500)
                    else:
                        self.root.after(200)  # Space between symbols
                self.root.after(400)  # Space between letters

    def play_beep(self, duration):
        def beep():
            winsound.Beep(self.pitch.get(), duration)

        thread = threading.Thread(target=beep)
        thread.start()


if __name__ == '__main__':
    root = tk.Tk()
    app = MorseCodeApp(root)
    root.mainloop()

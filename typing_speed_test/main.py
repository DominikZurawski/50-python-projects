import tkinter as tk
from tkinter import font

import time

def open_text():
    with open('text.txt') as f:
        lines = f.read()
        return lines

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', font="Helvetica", size=12, weight='bold'):
        super().__init__(master, font=(font, size, weight))
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class WordSpeedCounter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Word Speed Test")
        self.root.geometry("600x300")

        self.sample_text = open_text()
        self.text_list = self.sample_text.split()

        self.words_index = 0
        self.start_time = None
        self.words_typed = 0

        self.text_label = tk.Text(self.root, height=5, width=52, font = font.Font(family='Helvetica', size=12, weight='bold'))
        self.text_label.tag_configure("green", foreground="green")
        self.text_label.tag_configure("red", foreground="red")
        self.text_label.insert(tk.END, self.sample_text)
        self.text_label.pack()

        spacer = tk.Label(self.root, height=1)
        spacer.pack()

        self.entry = EntryWithPlaceholder(self.root, "type the words here")
        # self.entry = tk.Entry(self.root, font = font.Font(family='Helvetica', size=12, weight='bold'))
        # self.entry.insert(0, 'type the words here')
        self.entry.pack()
        self.entry.bind("<Key>", self.on_key_press)

        spacer = tk.Label(self.root, height=5)
        spacer.pack()

        self.time_remaining_label = tk.Label(self.root, text="Time: 60 s", font = font.Font(family='Helvetica', size=12, weight='normal'))
        self.time_remaining_label.pack()

        self.result_label = tk.Label(self.root, text="Words per minute: 0", font = font.Font(family='Helvetica', size=12, weight='normal'))
        self.result_label.pack()

        self.root.after(1000, self.update_timer)
        self.root.mainloop()

    def highlight(self, index, color="green", wrong_index=None):
        """Mark last correct word on green"""
        if 0 <= index < len(self.text_label.get("1.0", "end-1c").split()):

            content = self.text_label.get("1.0", "end-1c")
            words = content.split()
            start_index = content.index(words[index])
            end_index = start_index + len(words[index])
            self.text_label.tag_add(color, f"1.{start_index}", f"1.{end_index}")
            see_index = f"1.{end_index + 200}"
            self.text_label.see(see_index)
            if wrong_index:
                # self.text_label.tag_add("yellow", f"1.{start_index}", f"1.{end_index}")
                for i in wrong_index:
                    start_wrong_char = i + start_index
                    stop_wrong_char = start_wrong_char + 1
                    self.text_label.tag_add("red", f"1.{start_wrong_char}", f"1.{stop_wrong_char}")
                    self.text_label.see(see_index)
        else:
            pass
            # print("Incorrect index.")

    def compare_words(self, word1, word2):
        if len(word1) > len(word2):
            x = len(word1) - len(word2)
            for y in range(x):
                word2 += " "
        mismatch_indices = []
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                mismatch_indices.append(i)

        return mismatch_indices

    def on_key_press(self, event):
        if not self.start_time:
            self.start_time = time.time()

        typed_char = event.char
        # print(typed_char)
        if typed_char == " ":
            if self.text_list[self.words_index] == self.entry.get().strip():
                self.words_typed += 1
                self.display_results()
                self.highlight(self.words_index, "green")
            else:
                wrong_index = self.compare_words(self.text_list[self.words_index], self.entry.get().strip())

                self.highlight(self.words_index, wrong_index=wrong_index)
            self.words_index += 1
            self.entry.delete(0, tk.END)
            # self.highlight(self.words_index, "yellow")


    def update_timer(self):
        if self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            remaining_time = max(60 - elapsed_time, 0)
            self.time_remaining_label.config(text=f"Time: {remaining_time} s")

            # if remaining_time > 0:
            #     self.root.after(1000, self.update_timer)
            # else:
            if remaining_time == 0:
                self.display_results()
        self.root.after(1000, self.update_timer)

    def display_results(self):
        self.result_label.config(text=f"Words per minute: {self.words_typed}")

if __name__ == "__main__":
    WordSpeedCounter()

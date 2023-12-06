import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")

        self.music_file = None
        self.paused = False

        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self.root, text="Select Music", command=self.select_music)
        self.select_button.pack(pady=10)

        self.play_pause_button = tk.Button(self.root, text="Play", command=self.play_pause_music)
        self.play_pause_button.pack(pady=5)

        self.volume_label = tk.Label(self.root, text="Volume")
        self.volume_label.pack()

        self.volume_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(50)  # Set default volume to 50
        self.volume_slider.pack()

    def select_music(self):
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3")])

    def play_pause_music(self):
        if self.music_file:
            if not self.paused:
                pygame.mixer.init()
                pygame.mixer.music.load(self.music_file)
                pygame.mixer.music.set_volume(self.volume_slider.get() / 100)  # Set initial volume
                pygame.mixer.music.play()
                self.play_pause_button.config(text="Pause")
                self.paused = True
            else:
                pygame.mixer.music.pause()
                self.play_pause_button.config(text="Play")
                self.paused = False
        else:
            messagebox.showwarning("Warning", "Please select a music file first.")

    def set_volume(self, val):
        if self.music_file:
            volume = float(val) / 100
            pygame.mixer.music.set_volume(volume)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

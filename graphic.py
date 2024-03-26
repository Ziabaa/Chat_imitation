import tkinter as tk
import pygame



def play_audio(audio):
    pygame.mixer.init()  # Инициализация Pygame mixer
    pygame.mixer.music.load(audio)  # Загрузка аудиофайла
    pygame.mixer.music.play()  # Воспроизведение аудиофайла

def create_buttons_and_labels(messages, root):
    for i in range(len(messages)):
        if not i % 2 == 0:
            label = tk.Label(root, text=messages[i], font=("Arial", 12))
            button = tk.Button(root, text=f"Play client{i // 2}.mp3",
                               command=lambda audio=f"client{i // 2}.mp3": play_audio(audio))
            button.place(x=600, y=50 * i)
            label.place(x=0, y=50 * i)
        else:
            label = tk.Label(root, text=messages[i], font=("Arial", 12))
            label.place(x=160, y=50 * i)
            button = tk.Button(root, text=f"Play operator{i//2}.mp3",
                               command=lambda audio=f"operator{i//2}.mp3": play_audio(audio))
            button.place(x=0, y=50*i)

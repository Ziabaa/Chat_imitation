import tkinter as tk
import pygame
import json

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


# Создаем экземпляр класса Tk
root = tk.Tk()

# Путь к файлу, из которого будут импортированы данные
file_path = "messages.json"

# Импорт данных из файла в список
with open(file_path, 'r', encoding='utf-8') as file:
    messages = json.load(file)

# Устанавливаем размеры окна
root.geometry("700x500")

# Создание кнопок и меток с сообщениями
create_buttons_and_labels(messages, root)



create_buttons_and_labels(messages, root)

root.mainloop()

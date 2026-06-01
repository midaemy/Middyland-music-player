import tkinter as tk
import os
import pygame
from tkinter import filedialog

pygame.mixer.init()

root = tk.Tk()
root.title("Middyland Music Player")
root.geometry("400x300")
root.configure(bg="#e6dc77")

def choose_song():
    file_path = filedialog.askopenfilename(filetypes=[("Audiofiles", "*.mp3")])
    if file_path:
        pygame.mixer.music.load(file_path)
        name.config(text=os.path.basename(file_path))
        status.config(text="Song loaded! Click Play to start.")

def pause_song():
    pygame.mixer.music.pause()
    status.config(text="Song paused")
    play.config(text="▶Resume", command=resume_song)

def resume_song():
    pygame.mixer.music.unpause()
    status.config(text="Song playing")

def stop_song():
    pygame.mixer.music.stop()
    status.config(text="Song stopped")
    play.config(text="▶Play", command=play_song)

def play_song():
    pygame.mixer.music.play()
    status.config(text="Song playing")
    play.config(text="▶Play", command=play_song)
    if name.cget("text")=="Hooligan.mp3":
        root.configure(bg="#69020c")
        buttons_frame.configure(bg="#69020c")

        
status = tk.Label(root, text="Welcome to Middyland Music Player!", bg="#f28333", fg="white", font=("Arial", 12, "italic"))
status.pack(pady=20, fill="x", padx=20)

name = tk.Label(root, text="No songs choosen", bg="#f28333", fg="white", font=("Arial", 14, "bold"), wraplength=350)
name.pack(pady=5, padx=20, fill="x")

choose = tk.Button(root, text="🎶 Choose song (.mp3)", bg="#5ed4ff", fg="black", font=("Arial", 12, "bold"), command=choose_song)
choose.pack(pady=10)

buttons_frame = tk.Frame(root, bg="#e6dc77")
buttons_frame.pack(pady=20)

pause = tk.Button(buttons_frame, text="⏸Pause", bg="#80ff9d", fg="white", font=("Arial", 12, "bold"), width=10, command=pause_song)
pause.grid(row=0, column=0, padx=10)

play=tk.Button(buttons_frame, text="▶Play", bg="#b282ff", fg="white", font=("Arial", 12, "bold"), width=10, command=play_song)
play.grid(row=0, column=1, padx=10)

stop=tk.Button(buttons_frame, text="⏹Stop", bg="#fc818f", fg="white", font=("Arial", 12, "bold"), width=10, command=stop_song)
stop.grid(row=0, column=2, padx=10)

root.mainloop()
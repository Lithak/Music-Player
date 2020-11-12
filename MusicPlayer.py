from tkinter import *
import pygame
from pygame.locals import *
from tkinter import filedialog

root = Tk()
root.geometry("800x700")
root.title('Music Player')
root.configure(background='#7B5E7B')

# Initialize Pygame Mixer
pygame.mixer.init()


# Add Song function
def add_song():
    song = filedialog.askopenfilename(initialdir='Music/',
                                      title="Choose a Song",
                                      filetypes=(("mp3 Files", "*.mp3"),))

    # Strip out the directory info and .mp3 extension from the
    song = song.replace("/home/user/PycharmProjects/PlaySound/Music/", " ")
    song = song.replace("mp3", "")

    # Add song to listbox
    song_box.insert(END, song)


# Add many songs to play list
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='Music/',
                                        title="Choose a Song",
                                        filetypes=(("mp3 Files", "*.mp3"),))
    # loop thru song list & replace directory info & mp3
    for song in songs:
        song = song.replace("/home/user/PycharmProjects/PlaySound/Music/", " ")
        song = song.replace("mp3", "")
        # Add songs to listbox
        song_box.insert(END, song)


# Play selected song
def play():
    song = song_box.get(ACTIVE)
    song = f'/home/user/PycharmProjects/PlaySound/Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


# Stop playing song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


# Next song
def next():
    # get the current song number
    next_one = song_box.curselection()
    # add one to the current song number.
    next_one = next_one[0] + 1
    # grab tittle of song
    song = song_box.get(next_one)
    # add directory structure & mp3 to song tittle
    song = f'/home/user/PycharmProjects/PlaySound/Music/{song}.mp3'
    # load & play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # move Active bar
    song_box.selection_clear(0, END)
    # Activate new bar
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)


# Back song button
def back():
    # get the current song number
    next_one = song_box.curselection()
    # add one to the current song number.
    next_one = next_one[0] - 1
    # grab tittle of song
    song = song_box.get(next_one)
    # add directory structure & mp3 to song tittle
    song = f'/home/user/PycharmProjects/PlaySound/Music/{song}.mp3'
    # load & play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # move Active bar
    song_box.selection_clear(0, END)
    # Activate new bar
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)


# Delete a song in playlist
def delete_song():
    # delete current song selected
    song_box.delete(ANCHOR)
    # stop deleted song
    pygame.mixer.music.stop()


# Delete all songs
def delete_all():
    # delete current playlist
    song_box.delete(0, END)
    # stop deleted playlist
    pygame.mixer.music.stop()


# Create Global pause variable
global paused
paused = False


# Pause & unpause song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # pause
        pygame.mixer.music.pause()
        paused = True


# creating Playlist Box
song_box = Listbox(root, bg="#B8B8B8", fg="Grey", width=60, selectbackground='pink', selectforeground='black')
song_box.pack(pady=20)

#  Create Player control Images
back_btn = PhotoImage(file='/home/user/PycharmProjects/images/back50.png')
forward_btn = PhotoImage(file='/home/user/PycharmProjects/images/forward50.png')
play_btn = PhotoImage(file='/home/user/PycharmProjects/images/play50.png')
pause_btn = PhotoImage(file='/home/user/PycharmProjects/images/pause50.png')
stop_btn = PhotoImage(file='/home/user/PycharmProjects/images/stop50.png')

# Create Player control Frame
control_frame = Frame(root)
control_frame.pack()

# Create Player control Buttons
back_button = Button(control_frame, image=back_btn, borderwidth=0, background='#7B5E7B', command=back)
forward = Button(control_frame, image=forward_btn, borderwidth=0, background='#7B5E7B', command=next)
play_button = Button(control_frame, image=play_btn, borderwidth=0, background='#7B5E7B', command=play)
pause_button = Button(control_frame, image=pause_btn, borderwidth=0, background='#7B5E7B', command=pause)
stop_button = Button(control_frame, image=stop_btn, borderwidth=0, background='#7B5E7B', command=stop)

back_button.grid(row=0, column=0, padx=10)
forward.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu, background='#7B5E7B')

# Add Song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu, background='#7B5E7B')
add_song_menu.add_command(label="Add Song to Playlist", background='#7B5E7B', command=add_song)
# Add Many Songs
add_song_menu.add_command(label="Add  Many Songs to Playlist", background='#7B5E7B', command=add_many_songs)
# create a delete song manu
remove_song_manu = Menu(my_menu)
my_menu.add_cascade(label="remove Songs", menu=remove_song_manu)
remove_song_manu.add_command(label="Delete a song from playlist", command=delete_song)
remove_song_manu.add_command(label="Delete all songs from playlist", command=delete_all)
root.mainloop()

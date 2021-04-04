from tkinter import *
from tkinter import messagebox
import pafy


window = Tk()
window.iconphoto(False, PhotoImage(file='icon.jpg'))
window.title('  Audio/Video Downloader from Youtube')


# audio part
def audio():
    window.geometry('500x250')
    f1 = Frame().place(x=0, y=0, width=500, height=250)

    def downloader():
        try:
            url = str(link.get())
            pafy.new(url).getbestaudio(preftype='m4a').download()
            Label(f1, text='Download Successful', font='roboto').place(relx=0.5, rely=0.8, anchor=CENTER)
        except:
            messagebox.showinfo(title='Warning', message='Enter Something!')

    Label(f1, text='Youtube Audio Downloader', font=('roboto', 20)).place(relx=0.5, rely=0.1, anchor=CENTER)

    link = StringVar()
    Label(f1, text='Paste Link Here', font=('roboto', 15)).place(relx=0.5, rely=0.3, anchor=CENTER)
    Entry(f1, width=70, textvariable=link).place(x=32, y=90)
    Button(f1, text='Download', font=('roboto', 15), bg='red', fg='white', command=downloader).place(relx=0.4, rely=0.6,
                                                                                                     anchor=CENTER)
    Button(f1, text='Back', font=('roboto', 15), bg='black', fg='white', command=main_menu).place(relx=0.6, rely=0.6,
                                                                                                  anchor=CENTER)


# video part
def video():
    window.geometry('500x250')
    f1 = Frame().place(x=0, y=0, width=500, height=250)

    def downloader():
        try:
            url = str(link.get())
            pafy.new(url).getbestvideo(preftype='mp4').download()
            Label(text='Download Successful', font='roboto').place(relx=0.5, rely=0.8, anchor=CENTER)
        except:
            messagebox.showinfo(title='Warning', message='Enter Something New!')

    link = StringVar()
    Label(f1, text='Paste Link Here', font=('roboto', 15)).place(relx=0.5, rely=0.3, anchor=CENTER)
    Entry(f1, width=70, textvariable=link).place(x=32, y=90)
    Button(f1, text='Download', font=('roboto', 15), bg='red', fg='white', command=downloader).place(relx=0.4, rely=0.6,
                                                                                                 anchor=CENTER)
    Button(f1, text='Back', font=('roboto', 15), bg='black', fg='white', command=main_menu).place(relx=0.6, rely=0.6,
                                                                                              anchor=CENTER)


def main_menu():
    window.geometry('500x200')
    f1 = Frame().place(x=0, y=0, width=500, height=250)
    Label(f1, text='Youtube Audio/Video Downloader', font=('roboto', 20)).place(relx=0.5, rely=0.3, anchor=CENTER)
    audio_button = Button(f1, text='Audio Downloader', font=('roboto', 15), bg='red', fg='white', command=audio)
    audio_button .place(relx=0.3, rely=0.6, anchor=CENTER)
    video_button = Button(f1, text='Video Downloader', font=('roboto', 15), bg='red', fg='white', command=video)
    video_button.place(relx=0.7, rely=0.6, anchor=CENTER)


main_menu()
window.mainloop()

import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
import clipboard
import tkinter.filedialog as filedialog
import time

#============================
def DownloadVideo():
    try:
        ytLink = url_entry.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        output_path = entry_var.get()
        video.download(output_path)
    except Exception as e:
        print('Error:', str(e))

    
def PasteUrl():
    try:
        clipboard_content = clipboard.paste()  # Get content from clipboard
        url_var.set(clipboard_content)  # Set the clipboard content into the URL entry
    except Exception as e:
        print('Error pasting URL:', str(e))

def Destination_def():
    try:
        chosen_directory = filedialog.askdirectory()  # Open a folder selection dialog
        entry.delete(0, tk.END)  # Clear the current content of the entry field
        entry.insert(0, chosen_directory)  # Insert the chosen directory path into the entry field
    except Exception as e:
        print('Error choosing destination:', str(e))

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentageComplete = bytes_downloaded / total_size * 100
    per = str(int(percentageComplete))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    pg_bar.set(percentageComplete/100)
    app.update()  # Explicitly update the GUI
#============================
red = '#F60C28'
dark_grey = '#1A1A1A'
input_color = '#0D0D0D'

ctk.set_appearance_mode('dark')

# app
app = ctk.CTk()
app.geometry('700x470')
app.title('YOUTUBIFY V2.0')

# widgets
title = ctk.CTkLabel(app, text='YOUTUBIFY V2.0',font=('Montserrat',40,'bold'),text_color=red)
title.pack(pady = 30)

url_var = tk.StringVar()
url = ctk.CTkFrame(master=app,fg_color='transparent')
url.pack(pady = 10)

url_entry = ctk.CTkEntry(url, placeholder_text="insert the video url",width=463,height=46, corner_radius = 45, border_width = 0, fg_color = input_color,textvariable=url_var)
url_entry.pack(side = 'left', padx = 25)

paste_btn = ctk.CTkButton(url, text="PASTE",font=('Montserrat',22,'bold'),corner_radius=100,width=107,height=46,fg_color = red,hover_color='#090909', command=PasteUrl)
paste_btn.pack(side = 'left')

dest = ctk.CTkFrame(master = app, fg_color='transparent')
dest.pack(pady = 30)

entry_var = tk.StringVar()
entry = ctk.CTkEntry(dest, placeholder_text="insert the destination of downloaded video",width=439,height=46,corner_radius = 45, border_width = 0, fg_color = input_color, textvariable=entry_var)
entry.pack(side = 'left', padx = 25)

choose_btn = ctk.CTkButton(dest, text="CHOOSE",font=('Montserrat',22,'bold'),corner_radius=100, height=46,width=133, fg_color= red, hover_color='#090909', command=Destination_def)
choose_btn.pack(side = 'left')

down_button = ctk.CTkButton(app, text="DOWNLOAD",font=('Montserrat',22,'bold'),width=169,height=46,corner_radius=70,fg_color= red, hover_color='#090909', command=DownloadVideo)
down_button.pack(pady = 30)

# progress bar

pPercentage = ctk.CTkLabel(app, text='0%')
pPercentage.pack()

pg_bar = ctk.CTkProgressBar(app, orientation="horizontal",width=596,height=10,fg_color=input_color,progress_color=red)
pg_bar.set(0)
pg_bar.pack()



# run
app.mainloop()
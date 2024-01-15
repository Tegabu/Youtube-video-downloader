import tkinter 
import customtkinter
from pytube import YouTube
import os

script_directory = os.path.dirname(os.path.realpath(__file__))

# Download function
def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_complete_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        download_path = os.path.join(script_directory, video.title)

        title.configure(text=ytObject.title, text_color="white")
        downloadLabel.configure(text="")
        video.download(download_path)
        downloadLabel.configure(text ="Video Downloaded :)")
    except:
        downloadLabel.configure(text ="Download Failed", text_color="red")
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_downloaded = bytes_downloaded / total_size * 100
    per= str(int(percentage_downloaded))
    pCounter.configure(text=per + "%")
    pCounter.update()

#Systemm settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame

app = customtkinter.CTk();  
app.geometry("720x480")
app.title("YouTube Downloader")

#UI adds
title = customtkinter.CTkLabel(app, text = "Insert a YouTube link")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40,textvariable=url_var)
link.pack()

#Download Complete Alert
downloadLabel = customtkinter.CTkLabel(app, text ="")
downloadLabel.pack()

#Progress Count
pCounter = customtkinter.CTkLabel(app, text="0%")
pCounter.pack()

#Progress Bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Download Button
download = customtkinter.CTkButton(app, text = "Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()
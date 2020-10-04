from pytube import YouTube
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file_size = 0

def create_youtube_object(url, progress):
    return YouTube(url, on_progress_callback=progress).streams

def pick_resolution(streams, value):
    objects_with_res = [stream for stream in streams if stream.resolution == value]
    return objects_with_res[0]

def progress(stream=None, chunk=None,  remaining=None):
    file_downloaded = (file_size-remaining)
    per = round((file_downloaded/file_size)*100, 1)
    dBtn.config(text=f'{per}% downloaded')


def startDownload():
    global file_size
    try:
        print("Starting download")
        URL = urlField.get()
        resolution = resolutionField.get()
        dBtn.config(text='Please wait...')
        dBtn.config(state=DISABLED)
        path_save = askdirectory()
        if path_save is None:
            return
        stream_list = create_youtube_object(URL, progress)
        strm = pick_resolution(stream_list, resolution)
        import ipdb; ipdb.set_trace()
        x = ob.description.split("|")
        file_size = strm.filesize
        dfile_size = file_size
        dfile_size /= 1000000
        dfile_size = round(dfile_size, 2)
        label.config(text='Size: ' + str(dfile_size) + ' MB')
        label.pack(side=TOP, pady=10)
        desc.config(text=ob.title + '\n\n' + 'Label: ' + ob.author + '\n\n' + 'length: ' + str(round(ob.length/60, 1)) + ' mins\n\n'
                    'Views: ' + str(round(ob.views/1000000, 2)) + 'M')
        desc.pack(side=TOP, pady=10)
        strm.download(path_save, strm.title)
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", 'Downloaded Successfully')
        urlField.delete(0, END)
        label.pack_forget()
        desc.pack_forget()
        dBtn.config(text='Start Download')
        print("Finishing download")

    except Exception as e:
        print(e)
        print('Error!!')


def startDownloadthread():
    thread = Thread(target=startDownload)
    thread.start()


main = Tk()

main.title("My YouTube Downloader")
main.config(bg='#3498DB')

main.iconbitmap('images\\youtube-ios-app.ico')

main.geometry("500x600")

file = PhotoImage(
   file='images\\photo.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

urlField = Entry(main, font=("Times New Roman", 18), justify=CENTER)
urlField.insert(0, "URL do youtube")
urlField.pack(side=TOP, fill=X, padx=10, pady=15)

resolutionField = Entry(main, font=("Times New Roman", 18), justify=CENTER)
resolutionField.insert(0, "Resolução desejada, ex: 144p")
resolutionField.pack(side=TOP, fill=X, padx=10, pady=15)


dBtn = Button(main, text="Start Download", font=(
    "Times New Roman", 18), relief='ridge', activeforeground='red', command=startDownloadthread)
dBtn.pack(side=TOP)
label = Label(main, text='')
desc = Label(main, text='')
author = Label(main, text="@G.S.")
author.config(font=("Courier", 44))
author.pack(side=BOTTOM)
main.mainloop()

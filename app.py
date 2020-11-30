from tkinter import *
from tkinter import messagebox
from pytube import YouTube
window=Tk()
window.geometry('550x200')
def clear_fields():
    e1.delete(0,END)
    title_text.delete(1.0,END)
    views_text.delete(1.0,END)
    rating_text.delete(1.0,END)
    length_text.delete(1.0,END)
def download_Video():
    link=e1_Value.get()
    yt=YouTube(link)
    title_text.insert(END,yt.title)
    views_text.insert(END,yt.views)
    rating_text.insert(END,yt.rating)
    length_text.insert(END,yt.length)
    ys = yt.streams.get_by_itag('18')
    messagebox.showinfo("Downloading","Your Video is Downloading")
    ys.download()
    messagebox.showinfo("Completed",'Your Video is Downloaded')
l1=Label(window,text="Enter the Link of the Video:")
l1.grid(row=0,column=0)
e1_Value=StringVar()
e1=Entry(window,textvariable=e1_Value)
e1.grid(row=0,column=1)
b1=Button(window,text="Download",command=download_Video)
b1.grid(row=0,column=2)

b2=Button(window,text="Clear",command=clear_fields)
b2.grid(row=0,column=3)

title_label=Label(window,text="Title:")
title_label.grid(row=1,column=0)
title_text=Text(window,height=1,width=20)
title_text.grid(row=1,column=1)

views_label=Label(window,text="Views:")
views_label.grid(row=1,column=2)
views_text=Text(window,height=1,width=20)
views_text.grid(row=1,column=3)

length_label=Label(window,text="Length:")
length_label.grid(row=2,column=0)
length_text=Text(window,height=1,width=20)
length_text.grid(row=2,column=1)

rating_label=Label(window,text="Rating:")
rating_label.grid(row=2,column=2)
rating_text=Text(window,height=1,width=20)
rating_text.grid(row=2,column=3)
window.mainloop()
# link=input("Enter The Link of the Video:")
# yt=YouTube(link)
# print("Title: ",yt.title)
# print("Number of views: ",yt.views)
# print("Length of video: ",yt.length)
# print("Rating of video: ",yt.rating)
# print(yt.streams.filter(progressive=True))
# ys = yt.streams.get_by_itag('18')
# print("Downloading...")
# ys.download()
# print("Download completed!!")
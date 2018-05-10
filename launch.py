from tkinter import *
import time
import index
from tkinter.ttk import Progressbar
from tkinter import messagebox
import ubiquitalk

window = Tk()
window.title("EngtoTel Video Translator!")
window.geometry('355x480')
lbl = Label(window, text="English to Telugu Video Translator", bg="orange", font=("Arial Bold", 15), padx=5, pady=5)
lbl.grid(column=1, row=0)
lbl = Label(window, text="", font=("Arial Bold", 20), padx=5, pady=5)
lbl.grid(column=1, row=1)
lbl = Label(window, text="Please enter file name to process!", bg="lightblue", font=("Arial Bold", 8), padx=5, pady=5)
lbl.grid(column=1, row=2)
lbl = Label(window, text="", font=("Arial Bold", 20), padx=5, pady=5)
lbl.grid(column=1, row=3)
lbl = Label(window, text="File Name (including extension) ")
lbl.grid(column=1, row=4)
txt = Entry(window, width=20)
txt.grid(column=1, row=5)


def clicked():
    """
    Send request to the index function to perform the needy.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    res = "Processing " + txt.get() + "..."
    outputval = index.main(str(txt.get()))
    # lbl.configure(text= res)
    # lbl.configure(text="Your output file is ready!")
    if outputval == 0:
        messagebox.showinfo('Processing Done!','Output file has been generated! Thank you for using the application!')
        print("Output ready!")
    elif outputval == 1:
    	messagebox.showinfo("Format unsupported!", 'Unfortunately, we only accept mp4 files as of now!')
    elif outputval == 2:
    	messagebox.showinfo("File too big!", 'Please use a smaller file! Anything below 8 minutes should be fine!')
    else:
    	messagebox.showinfo("Unknown Error!", 'Unknown error has occured. We will investigate it!')

def launch():
	ubiquitalk.main()

lbl = Label(window, text="", font=("Arial Bold", 15), padx=5, pady=5)
lbl.grid(column=1, row=6)
btn = Button(window, text="Translate!", command=clicked)
btn.grid(column=1, row=7)
lbl = Label(window, text="", font=("Arial Bold", 20), padx=5, pady=5)
lbl.grid(column=1, row=8)
lbl = Label(window, text="Developed by", font=("Trebuchet Bold", 7), padx=5, pady=5)
lbl.grid(column=1, row=9)
lbl = Label(window, text="Srikar Kashyap Pulipaka", font=("Arial Bold", 7), padx=5, pady=5)
lbl.grid(column=1, row=10)
lbl = Label(window, text="Surya Sai Mourya Kosaraju", font=("Arial Bold", 7), padx=5, pady=5)
lbl.grid(column=1, row=11)
lbl = Label(window, text="Chaitanya Krishna Kasaraneni", font=("Arial Bold", 7), padx=5, pady=5)
lbl.grid(column=1, row=12)
lbl = Label(window, text="Sandeep Vemulapalli", font=("Arial Bold", 7), padx=5, pady=5)
lbl.grid(column=1, row=13)
lbl = Label(window, text="@KL University (KLEF) via KLGLUG May 2017", font=("Arial Bold", 7), padx=5, pady=5)
lbl.grid(column=1, row=14)
lbl = Label(window, text="special thanks to Dr. Alan Black at Carnegie Mellon University", font=("Arial Bold", 7), padx=5, pady=5)
lbl.grid(column=1, row=15)
#btn = Button(window, text="Launch Ubiquitalk!", command=launch)
#btn.grid(column=1, row=16)
window.mainloop()

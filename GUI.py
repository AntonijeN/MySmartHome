import tkinter as tk
from tkinter import HORIZONTAL, ttk as ttk
import datetime as dt
from time import strftime







root = tk.Tk()
root.title("My Smart TV Controler")

date = dt.datetime.now()


def tframe():

    time = strftime("%H:%M:%S")
    time1 = tk.Label(root,
    text=f"{time}",
    font="Calibri, 20"
    )
    time1.config(text=time)
    time1.after(1000, tframe)

    time1.grid(row=0, column=1, padx=10, pady=10)

def dframe():
    dateTimeFrame= tk.Label(root,
    text=f"{date:%A, %B %d, %Y}",
    font="Calibri, 20"
    )
    dateTimeFrame.grid(row=0, column=1, padx=10, pady=10)


def notebook():
    notebook = ttk.Notebook(root)
    notebook.grid(row=0, column=0, padx=10, pady=10)


    tv_dnevni_boravak = tk.Label(notebook, 
    text = "Tv u dnevnom boravku",
    bg="blue",
    fg="white",
    width=5,
    height=5,
    activebackground="orange",
    font="Helvetica, 14"
    )

    tv_dnevni_boravak.grid(row=0, column=0, pady=20)
    notebook.add(tv_dnevni_boravak, text = "Tv dnevni boravak")

    tv_spavaca_soba = tk.Label(notebook,
    text="Tv u spavacoj sobi",
    bg="blue",
    fg="white",
    width=5,
    height=5,
    activebackground="orange",
    font="Helvetica, 14"
    )

    tv_spavaca_soba.grid(row=0, column=1, pady=20)
    notebook.add(tv_spavaca_soba, text="Tv spavaca soba")
    tv_djecja_soba = tk.Label(notebook,
    text="Tv u djecjoj sobi",
    bg="blue",
    fg="white",
    width=20,
    height=5,
    activebackground="orange",
    font="Helvetica, 14"
    )

    tv_djecja_soba.grid(row=0, column=2, pady=20)
    notebook.add(tv_djecja_soba, text="Tv djecja soba")

    setting_frame = tk.Frame(root,
    width=20,
    height=5
    )

    setting_frame.grid(row=0, column=3, padx=5, pady=10)
    notebook.add(setting_frame, text="Settings")
    
    time_check = tk.Checkbutton(setting_frame, 
    text="With time",
    width=20,
    height=5,
    activebackground="orange",
    font="Helvetica, 14",
    command=tframe,
    onvalue=True, 
    offvalue=False
    )
    time_check.grid(row=0, column=0, padx=10, pady=10)
    
    change_color = tk.Button(setting_frame,
    text="Change color",
    width=20,
    height=5,
    activebackground="orange",
    font="Helvetica, 14")
    change_color.grid(row=1, column=0, padx=10, pady=10)



def control_frame():

    kontrole_frame = tk.Frame(root,
    borderwidth=3,
    width=250,
    height=400
    )
    kontrole_frame.grid(column=0, row=1, padx=10, pady=10)

    upali_tv = tk.Button(kontrole_frame,
    text= "Uključeno",
    bg="yellow",
    fg="black",
    font="Helvetica 10 bold",
    activebackground="red",
    width=20,
    height=5
    )

    upali_tv.grid(row=0, column=0, padx=10, pady=10,)

    ugasi_tv = tk.Button(kontrole_frame,
    text= "Isključeno",
    bg="yellow",
    fg="black",
    font="Helvetica 10 bold",
    activebackground="red",
    width=20,
    height=5
    )

    ugasi_tv.grid(row=1, column=0, padx=10, pady=10)

def volume_controle():
    kontrole_frame = tk.Frame(root,
    borderwidth=3,
    width=250,
    height=400
    )
    kontrole_frame.grid(column=1, row=1, padx=10, pady=10)
    

    volume_controle = tk.Label(kontrole_frame,
    text="Volume",
    font="Helvetica 20 italic")

    volume_controle.grid(row=1, column=1, padx=10, pady=10)

    volume_slide = tk.Scale(root,
    bg="orange",
    fg="white",
    from_=0,
    to_=100,
    orient=HORIZONTAL
    )
    volume_slide.grid(row=1, column=2, padx=10, pady=10)


notebook()
#dframe()
#tframe()
control_frame()
volume_controle()
root.mainloop()

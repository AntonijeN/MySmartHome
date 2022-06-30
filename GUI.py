import tkinter as tk
from tkinter import ttk as ttk





root = tk.Tk()
root.title("My Smart TV Controler")

def notebook():
    notebook = ttk.Notebook(root)
    notebook.grid(row=0, column=0, padx=10, pady=10)


    tv_dnevni_boravak = tk.Button(notebook, 
    text = "Tv u dnevnom boravku",
    bg="blue",
    fg="white",
    width=20,
    height=5,
    activebackground="orange",
    font="Helvetica, 14"
    )

    tv_dnevni_boravak.grid(row=0, column=0, pady=20)

    tv_spavaca_soba = tk.Button(notebook,
    text="Tv u spavacoj sobi",
    bg="blue",
    fg="white",
    width=20,
    height=5,
    activebackground="orange",
    font="Helvetica, 14"
    )

    tv_spavaca_soba.grid(row=0, column=1, pady=20)

    tv_djecja_soba = tk.Button(notebook,
    text="Tv u djecjoj sobi",
    bg="blue",
    fg="white",
    width=20,
    height=5,
    activebackground="orange",
    font="Helvetica, 14"
    )

    tv_djecja_soba.grid(row=0, column=2, pady=20)

def control_frame():

    kontrole_frame = tk.Frame(root,
    borderwidth=3,
    width=250,
    height=400
    )
    kontrole_frame.grid(rowspan=2, columnspan=10, column=0, row=1, padx=10, pady=10)

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
    kontrole_frame.grid(rowspan=2, columnspan=2, column=1, row=1, padx=10, pady=10)
    

    volume_controle = tk.Label(kontrole_frame,
    text="Volume",
    font="Helvetica 20 italic")

    volume_controle.grid(row=1, column=1, padx=10, pady=10)



notebook()
control_frame()
volume_controle()
root.mainloop()

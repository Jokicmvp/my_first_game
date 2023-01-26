import tkinter as tk

root = tk.Tk()
root.title("рпррргпгрраеер")
root.geometry("500x500")
root.resizable(False, False)
root.config(background="beige")

label = tk.Label(text="заполните анкету", background="beige", font="Comic 30")
label.pack(anchor="center")

entry_fio = tk.Entry(font="comic 25")
entry_age = tk.Entry(font="comic 25")
entry_class = tk.Entry(font= "comic 25")
entry_fio.pack(anchor= "center", pady=10)
entry_age.pack(anchor="center", pady=10)
entry_class.pack(anchor="center", pady=10)
root.mainloop()


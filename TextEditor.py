import tkinter as tk
from tkinter import filedialog

def open_file():
    file_name = filedialog.askopenfilename(defaultextension="txt",
                                           title="Open file",
                                           filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_name:
        f = open(file_name, "r", encoding="utf-8")
        text_read = f.read()
        if text_read != None:
            text.delete(1.0, "end")
            text.insert("end", text_read)
        f.close()

def save_file():
    file_name = filedialog.asksaveasfilename(defaultextension="txt",
                                             title="Save file",
                                             filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_name:
        f = open(file_name, "w", encoding="utf-8")
        f.write(text.get(1.0, "end"))
        f.close()

def about():
    win_about = tk.Tk()
    win_about.geometry("200x150")
    win_about.title("About")

    lab = tk.Label(win_about, text="IT STEP, Gr 1111", pady=20)
    lab.pack()
    win_about.mainloop()


window = tk.Tk()
window.geometry("600x400+400+200")
window.minsize(200, 200)
window.title("Text Editor")

img1 = tk.PhotoImage(file="img/folder-open-outline-custom.png")
img2 = tk.PhotoImage(file="img/content-save-outline-custom.png")

menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New", compound="left")
file_menu.add_command(label="Open...", compound="left", command=open_file, image=img1, accelerator="Ctrl+O")
# window.bind_all("<Control-o>", open_file)
file_menu.add_command(label="Save As...", compound="left", command=save_file, image=img2, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit")
menu.add_cascade(label="File", menu=file_menu)

about_menu = tk.Menu(menu, tearoff=0)
about_menu.add_command(label="Help")
about_menu.add_command(label="About", command=about)
menu.add_cascade(label="Help", menu=about_menu)

text = tk.Text(window)
text.pack(fill="both", expand=1)



window.mainloop()
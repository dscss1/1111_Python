import tkinter as tk

# window = tk.Tk()
#
# window.title("Game")
# window.geometry("600x400+600+300")
# # window.resizable(False, False)
# window.minsize(300, 300)
#
# label = tk.Label(window, text="Hello",
#                  font=("Comic Sans MS", 16, "bold"),
#                  fg="Tomato",
#                  bg="yellow",
#                  width=20,
#                  height=2)
# label.pack()
#
# btn = tk.Button(window, text="Click")
# btn.pack()
#
# window.mainloop()

time = 100
score = 0
press_enter = True

window = tk.Tk()

window.title("Game")
window.geometry("600x600+600+100")
window.resizable(False, False)
window.iconbitmap("pics/bomb.ico")

label = tk.Label(window, text="Для початку гри натисніть [ENTER]", font=("Comic Sans MS", 12, "bold"))
label.pack()

label_time = tk.Label(window, text=f"Залишок часу {time}", font=("Comic Sans MS", 16, "bold"))
label_time.pack()

label_score = tk.Label(window, text=f"Набрані бали {score}", font=("Comic Sans MS", 16, "bold"))
label_score.pack()

img1 = tk.PhotoImage(file="pics/1.gif")


label_bomb = tk.Label(window, image=img1)
label_bomb.pack()

click = tk.Button(window, text="Тикай сюди", font=("Comic Sans MS", 16, "bold"), bg="black", fg="white")
click.pack()



window.mainloop()
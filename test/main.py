import tkinter as tk
import tkinterweb as webside
import time as gold



app = tk.Tk()
app.title("Nanthanda leo")
app.state("zoomed")


frames = tk.PanedWindow(app , orient=tk.HORIZONTAL)
frames.pack(fill=tk.BOTH,expand=True)


left = tk.Frame(frames , bg="lightblue")
tk.Label(left , text="Santhosh").pack()


right = tk.Frame(frames , bg="red")
tk.Label(right , text="Ashwin Arul").pack()

frames.add(left , width = 300)
frames.add(right)


app.mainloop()


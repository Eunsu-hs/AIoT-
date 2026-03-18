import tkinter

window = tkinter.Tk()
window.title("CPU TEMPERATURE")
window.geometry("400x100")
window.resizable(False,False)

label=tkinter.Label(window, text="hello")
label.pack()

window.mainloop()
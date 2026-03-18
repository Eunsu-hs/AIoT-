import tkinter
import os
import time

def time1000mS():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=","").replace("'C","")
    print(temp)
    label.config(text=temp)
    window.after(1000,time1000mS)

window = tkinter.Tk()
window.title("CPU TEMPERATURE")
window.geometry("400x100")
window.resizable(False,False)

label=tkinter.Label(window, text="hello")
label.pack()

time1000mS()

window.mainloop()

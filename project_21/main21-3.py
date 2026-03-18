import tkinter
import tkinter.font
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

font = tkinter.font.Font(size = 30)
label=tkinter.Label(window, text="hello", font=font)
label.pack()

time1000mS()

window.mainloop()


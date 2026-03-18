import tkinter
import tkinter.font
import os
import time
from gpiozero import Motor

motor = Motor(21, 20)

def time1000mS():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=","").replace("'C","")
    temp = float(temp)
    print(temp)
    fanSpeed = "0%"
    if temp < 40 :
        motor.forward(0.4)
        fanSpeed = "0%"
    elif temp >= 40 and temp < 59:
        motor.forward(0.7)
        fanSpeed = "70%"
    elif temp >= 60:
        motor.forward(1.0)
        fanSpeed = "100%"
    display = str(temp) + "C" + "   " + fanSpeed
    label.config(text=display)
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


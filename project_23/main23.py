import tkinter
import tkinter.font
from gpiozero import LED

redLedPin = LED(23)
greenLedPin = LED(24)

def redLedOn():
    redLedPin.on()

def redLedOff():
    redLedPin.off()
    
def greenLedOn():
    greenLedPin.on()

def greenLedOff():
    greenLedPin.off()

window = tkinter.Tk()
window.title("LED FAN CONTROL")
window.geometry("400x400")
window.resizable(False,False)

font = tkinter.font.Font(size = 15)
redLedLabel=tkinter.Label(window, text="RED LED", font=font)
redLedOnBtn = tkinter.Button(window, width = 6, height = 2, text="on", command=redLedOn)
redLedOffBtn = tkinter.Button(window, width = 6, height = 2, text="off", command=redLedOff)
greenLedLabel=tkinter.Label(window, text="GREEN LED", font=font)
greenLedOnBtn = tkinter.Button(window, width = 6, height = 2, text="on", command=greenLedOn)
greenLedOffBtn = tkinter.Button(window, width = 6, height = 2, text="off", command=greenLedOff)

redLedLabel.grid(row = 0, column = 0)
redLedOnBtn.grid(row = 0, column = 1)
redLedOffBtn.grid(row = 0, column = 2)
greenLedLabel.grid(row = 1, column = 0)
greenLedOnBtn.grid(row = 1, column = 1)
greenLedOffBtn.grid(row = 1, column = 2)

window.mainloop()

import tkinter
import tkinter.font
from gpiozero import LED,Motor

redLedPin = LED(23)
greenLedPin = LED(24)

motor = Motor(21, 20)

def redLedOn():
    redLedPin.on()

def redLedOff():
    redLedPin.off()
    
def greenLedOn():
    greenLedPin.on()

def greenLedOff():
    greenLedPin.off()
    
def fanSpeed(self):
    value = scale.get() / 100.0
    print(value)
    motor.forward(value)

window = tkinter.Tk()
window.title("LED FAN CONTROL")
window.geometry("400x400")
window.resizable(False,False)

font = tkinter.font.Font(size = 15)
redLedLabel = tkinter.Label(window, text="RED LED", font=font)
redLedOnBtn = tkinter.Button(window, width = 6, height = 2, text="on", command=redLedOn)
redLedOffBtn = tkinter.Button(window, width = 6, height = 2, text="off", command=redLedOff)
greenLedLabel = tkinter.Label(window, text="GREEN LED", font=font)
greenLedOnBtn = tkinter.Button(window, width = 6, height = 2, text="on", command=greenLedOn)
greenLedOffBtn = tkinter.Button(window, width = 6, height = 2, text="off", command=greenLedOff)

fanLabel = tkinter.Label(window, text="FAN SPEED", font=font)
var = tkinter.IntVar()
scale = tkinter.Scale(window, variable=var, command=fanSpeed, orient="horizontal",
                      showvalue=False,tickinterval=10,to=100, length=300)

redLedLabel.grid(row = 0, column = 0)
redLedOnBtn.grid(row = 0, column = 1)
redLedOffBtn.grid(row = 0, column = 2)
greenLedLabel.grid(row = 1, column = 0)
greenLedOnBtn.grid(row = 1, column = 1)
greenLedOffBtn.grid(row = 1, column = 2)
fanLabel.grid(row = 2, column = 0, columnspan=3)
scale.grid(row = 3, column = 0, columnspan=3)

window.mainloop()
from flask import Flask
from gpiozero import LED

app = Flask(__name__)

red_led = LED(21)   

@app.route('/')
def flask():
   return "hello Flask"

@app.route('/ledon')
def ledOn():
   red_led.on()    
   return "<h1> LED ON </h1> "

@app.route('/ledoff')
def LedOff():
   red_led.off()      
   return "<h1> LED OFF </h1>"

if __name__ == "__main__":
   app.run(host = "0.0.0.0", port = "80")